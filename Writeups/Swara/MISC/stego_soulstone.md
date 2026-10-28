# Stego_SoulStone (Misc / Steganography, Medium-Hard)

**Author:** Swara Shirke  
**Category:** Misc / Steganography  
**Difficulty:** Medium–Hard  
**Theme:** Ghost Protocol / Soul Stone  
**Flag Format:** `OWASP{...}`

---

## Challenge Description

> An ordinary-looking server log was recovered from an active node. The visible log does not directly reveal any secret, but something lingers beneath the surface.
>
> The log was copied exactly as it was found — nothing was cleaned or modified.
>
> **Task:** Investigate the artifact, uncover the hidden data channel, and recover the flag.

**Challenge Files:**
- `README.txt` — Challenge briefing and context.
- `server.log` — The main artifact containing hidden data.
- `hints.txt` — Progressive hints.

---

## Summary

*Stego_SoulStone* utilizes whitespace steganography embedded at the end of log lines. By interpreting trailing spaces as `0` and trailing tabs as `1`, a binary stream is extracted and decoded into an ASCII Base64 string. Decoding the Base64 payload yields encrypted bytes, which are then decrypted using a repeating-key XOR with the key `PHANTOM` (discovered from a legacy diagnostic codename inside `server.log`).

---

## Flag

```text
OWASP{the_soul_remembers}
```

---

## Solve Flow

```text
server.log ➔ Trailing Spaces/Tabs ➔ Binary Stream ➔ ASCII ➔ Base64 String ➔ Base64 Decode ➔ XOR with "PHANTOM" ➔ Flag
```

---

## Step-by-Step Solution

### Step 1 — Inspect Whitespace in the Log
Opening `server.log` with whitespace visualization enabled (e.g., in VS Code via `"editor.renderWhitespace": "all"`) reveals variable trailing whitespace characters on select lines.

The encoding scheme:
* `SPACE` = `0`
* `TAB` (`\t`) = `1`

### Step 2 — Extract Binary Bits
Parsing the trailing whitespace across the log lines yields an ordered bitstream:

```python
with open("server.log", "r") as f:
    lines = f.readlines()

bits = ""
for line in lines:
    raw_trailing = line.rstrip("\r\n")
    trailing_ws = raw_trailing[len(raw_trailing.rstrip(" \t")):]
    for ch in trailing_ws:
        if ch == " ":
            bits += "0"
        elif ch == "\t":
            bits += "1"
```

### Step 3 — Binary to ASCII (Base64 String)
Grouping the extracted bits into 8-bit bytes produces an ASCII string:

```text
Hx8AHQQ0OTgtHiI7KBInKTIROio7NToeKzk/OSk1
```

### Step 4 — Base64 Decoding
Decoding the string reveals an obfuscated byte sequence:

```python
import base64

raw_b64 = "Hx8AHQQ0OTgtHiI7KBInKTIROio7NToeKzk/OSk1"
ciphertext = base64.b64decode(raw_b64)
# b'\x1f\x1f\x00\x1d\x04498-\x1e\";(\x12\')2\x11:*;5:\x1e+9?9)5'
```

### Step 5 — Discovering the XOR Key
Inspecting the visible lines in `server.log` reveals a diagnostic message:

```text
[DEBUG] Legacy diagnostic codename: PHANTOM.
```

### Step 6 — Decryption
Applying repeating XOR with key `PHANTOM`:

```python
key = b"PHANTOM"
plaintext = bytes(b ^ key[i % len(key)] for i, b in enumerate(ciphertext))
print(plaintext.decode())
```

**Output:**
```text
OWASP{the_soul_remembers}
```

---

## Key Takeaways
1. Whitespace can serve as an invisible covert communication channel in plain text files.
2. Steganography often chains encoding (Base64) with basic cryptography (XOR).
3. Context clues inside logs (such as codenames or error messages) often reveal decryption keys.
