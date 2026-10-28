# Contributing to ByteMeCTF Writeups

Thank you for contributing challenge solutions and official writeups to the **ByteMeCTF** repository. This guide outlines repository standards, formatting templates, and the Pull Request workflow for challenge authors and contributors.

---

## Repository Directory Structure

All writeups live inside the `Writeups/` directory, organized by author handle and challenge category:

```text
Writeups/
└── <author-handle>/
    └── <Category>/
        ├── <challenge_name>.md
        └── resources/
            ├── screenshot_01.png
            └── solve_script.py
```

### Standard Categories:
* `Web` — Web Exploitation, API security, SSRF, SSTI, XSS, Session Hijacking
* `Crypto` — Cryptography, Custom Ciphers, RSA, Discrete Logarithms, Graph Key Derivation
* `Pwn` — Binary Exploitation, ROP, Format Strings, Heap, Buffer Overflows
* `Reverse` / `Mobile` — Reverse Engineering, Stripped Binaries, Custom VMs, Android APKs, JNI
* `Forensics` — Digital Forensics, Memory Dumps (Volatility), PCAP Analysis, Disk Images
* `OSINT` — Open Source Intelligence, Geolocation, Satellite Recon, Footprinting
* `Misc` / `Stego` — Steganography, Audio, QR Reconstruction, Scripting
* `AI` — LLM Jailbreaking, Prompt Injection, Adversarial Machine Learning

---

## Contributor Workflow

### 1. Fork and Clone
```bash
# Clone your personal fork
git clone https://github.com/<your-username>/ByteMeCTF-WriteUps.git
cd ByteMeCTF-WriteUps

# Add upstream remote
git remote add upstream https://github.com/suyog-jadhav/ByteMeCTF-WriteUps.git
```

### 2. Branch from Main
Always ensure your `main` branch is in sync with upstream before creating a branch:
```bash
git checkout main
git pull upstream main
git checkout -b <your-name>/<category>-<challenge-name>
```

### 3. Folder & File Conventions
* Use lowercase snake_case for markdown files: `sqli_0.md`, `stalker_0.md`.
* Store all screenshots, pcaps, and solver scripts inside a `resources/` folder in the same directory.
* Embed media using relative paths: `![Step Screenshot](resources/screenshot1.png)`.

---

## Writeup Markdown Template

Every challenge writeup should follow this structured template:

```markdown
# Challenge Name (Category, Difficulty)

**Author:** Your Name  
**Category:** Category Name  
**Difficulty:** Easy / Medium / Hard / Expert / Insane  
**Flag Format:** `OWASP{...}` or `CTF{...}`

---

## Challenge Description

> Paste the exact in-game challenge description or briefing here.

**Attachment:** `challenge.zip` (or external link if large)

---

## Summary

A 2-3 sentence executive summary explaining the high-level vulnerability, intended vector, and the solution strategy. No spoilers in the first sentence.

---

## Flag

\`\`\`text
OWASP{recovered_flag_here}
\`\`\`

---

## Step 1 — Initial Reconnaissance & Discovery

Detailed technical breakdown of the initial inspection, tools run, or source code analysis.

\`\`\`bash
# Commands executed
file target_binary
checksec --file=target_binary
\`\`\`

![Initial Recon](resources/recon_screenshot.png)

---

## Step 2 — Vulnerability Analysis & Exploitation

Walkthrough of discovering the flaw and formulating the exploit.

\`\`\`python
# Snippet or explanation of solve script
\`\`\`

---

## Tools Used

* **Tool 1** — Purpose (e.g., Ghidra for native disassembly)
* **Tool 2** — Purpose (e.g., CyberChef for decoding)
* **Tool 3** — Purpose (e.g., Python `pwntools`)

---

## Timeline / Methodology Summary

| Step | Action | Result |
|:---:|---|---|
| 1 | File inspection | Identified stripped 64-bit ELF |
| 2 | Static analysis | Located custom VM opcode dispatch |
| 3 | Solver script execution | Recovered the flag |
```

---

## Quality Checklist Before Opening a PR

- [ ] Folder structure matches `Writeups/<author>/<Category>/`
- [ ] Filenames use lowercase snake_case (`challenge_name.md`)
- [ ] All images are placed inside `resources/` and referenced with relative paths
- [ ] Flag is shown in a designated code block
- [ ] Working exploit/solver script is included either inline or as a file in `resources/`
- [ ] No extraneous personal files, virtualenvs (`.venv`), or compiled binaries that are already generated
- [ ] Clear commit message (e.g., `feat: add web-signal-console writeup by pratik`)

---

## Authors & Maintainers

Maintained by **Suyog Jadhav** and the **OWASP PCCOE Team**.  
Have questions? Reach out in the OWASP PCCOE community or open an Issue.
