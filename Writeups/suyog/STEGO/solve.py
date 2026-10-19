
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE = "soul_stone_graph.png"

# These limits come from the original graph generator.
XMIN, XMAX = -2, 41
YMIN, YMAX = 25, 135
FLAG_LENGTH = 40

img = cv2.imread(IMAGE)
if img is None:
    raise SystemExit(f"Cannot open {IMAGE}")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Select the graph's plotting area interactively.
fig, ax = plt.subplots(figsize=(14, 8))
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax.set_title(
    "Click TOP-LEFT and BOTTOM-RIGHT corners of the plot area"
)
corners = plt.ginput(2, timeout=0)
plt.close(fig)

if len(corners) != 2:
    raise SystemExit("Please select both plot corners.")

(x1, y1), (x2, y2) = corners
left, right = sorted([int(x1), int(x2)])
top, bottom = sorted([int(y1), int(y2)])

# Flag points were gray with alpha=0.75.
# White decoys were plotted with alpha=0.22.
# This threshold is only a heuristic.
crop = gray[top:bottom, left:right]
_, mask = cv2.threshold(crop, 80, 255, cv2.THRESH_BINARY)

# Remove tiny isolated pixels.
count, labels, stats, centers = cv2.connectedComponentsWithStats(
    mask, connectivity=8
)

candidates = []

height, width = crop.shape

for i in range(1, count):
    x, y, w, h, area = stats[i]

    # Candidate marker-sized blobs; tune after inspecting the output.
    if not (2 <= area <= 100 and 2 <= w <= 15 and 2 <= h <= 15):
        continue

    cx, cy = centers[i]

    # Convert pixel position to graph data coordinates.
    data_x = XMIN + (cx / width) * (XMAX - XMIN)
    data_y = YMAX - (cy / height) * (YMAX - YMIN)

    if 32 <= data_y <= 126:
        candidates.append((data_x, data_y, area))

# For each expected integer X, print nearby candidates.
print("\nCandidate ASCII values by X position:")
recovered = []

for index in range(FLAG_LENGTH):
    nearby = [
        (x, y, area)
        for x, y, area in candidates
        if abs(x - index) < 0.35
    ]

    if not nearby:
        print(f"{index:02}: no candidate")
        recovered.append(None)
        continue

    # Prefer the candidate closest to the expected integer X.
    x, y, area = min(nearby, key=lambda p: abs(p[0] - index))
    value = round(y)

    char = chr(value) if 32 <= value <= 126 else "?"
    print(
        f"{index:02}: x={x:.2f}, y={y:.2f}, "
        f"ASCII={value}, char={char!r}"
    )
    recovered.append(value)

print("\nDecoded candidate:")
print("".join(chr(v) if v is not None else "?"
              for v in recovered))

# Save the threshold mask for visual debugging.
cv2.imwrite("threshold_mask.png", mask)
print("\nSaved threshold_mask.png")
