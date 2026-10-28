<div align="center">

# 💎 ByteMeCTF 2026 — Official Challenge Solutions

### The Definitive Writeups Archive by the OWASP PCCOE Team

[![Event](https://img.shields.io/badge/Event-ByteMeCTF_2026-orange?style=for-the-badge&logo=target)](https://github.com/suyog-jadhav/ByteMeCTF-WriteUps)
[![Organized by](https://img.shields.io/badge/Organized_By-OWASP_PCCOE-blue?style=for-the-badge&logo=owasp)](https://github.com/suyog-jadhav/ByteMeCTF-WriteUps)
[![Challenges](https://img.shields.io/badge/Challenges-69_Writeups-success?style=for-the-badge&logo=hackthebox)](CATEGORY_INDEX.md)
[![Categories](https://img.shields.io/badge/Categories-8_Domains-purple?style=for-the-badge)](CATEGORY_INDEX.md)
[![Authors](https://img.shields.io/badge/Authors-20_Creators-informational?style=for-the-badge&logo=github)](AUTHORS.md)
[![Status](https://img.shields.io/badge/Status-Complete_&_Verified-brightgreen?style=for-the-badge)](#)

<p align="center">
  <b>Welcome participants!</b> Here you will find the complete, step-by-step official writeups, exploit scripts, proof-of-concepts, and architectural post-mortems for all challenges featured in <b>ByteMeCTF 2026</b>.
</p>

---

### ⚡ Quick Navigation

[**📂 Full Category Index**](CATEGORY_INDEX.md) • [**👥 Authors Directory**](AUTHORS.md) • [**🏆 Featured Campaigns**](#-featured-campaign-missions) • [**📄 Word Docs (.docx)**](Writeups/pratik/Word_Documents/) • [**🤝 Contributing Guide**](CONTRIBUTING.md)

</div>

---

## 📊 Competition Overview & Statistics

ByteMeCTF 2026 was themed around the mystery and trials of Vormir and the Soul Stone, challenging participants across web vulnerabilities, memory dumps, custom bytecode virtual machines, graph-based cryptography, hardware reflection, and OSINT investigations.

| Category | Challenge Count | Difficulty Range | Primary Focus |
|---|:---:|:---:|---|
| [🌐 **Web Exploitation**](#-web-exploitation) | **13** | Easy → Expert | SSTI, Race Conditions, Parser Differentials, SSRF, JWT, IDOR |
| [💥 **Pwn / Binary Exploitation**](#-pwn--binary-exploitation) | **5** | Easy → Hard | Buffer Overflows, Format Strings, GOT Overwrite, Stack Canary ROP, Heap |
| [🔓 **Reverse Engineering & Mobile**](#-reverse-engineering--mobile) | **7** | Easy → Insane | Custom VM Bytecode, JNI Native Obfuscation, Frida Hooking, Go Reversing |
| [🔐 **Cryptography**](#-cryptography) | **6** | Medium → Hard | Hamiltonian Graph Traversal, Affine Ciphers, RSA Common Modulus, ECC DLog |
| [🔍 **Digital & Network Forensics**](#-digital--network-forensics) | **7** | Easy → Hard | Volatility 3 Memory Dumps, TLS PCAP Decryption, Covert Channels, Disk Images |
| [🛰️ **Open Source Intelligence (OSINT)**](#-open-source-intelligence-osint) | **17** | Easy → Expert | The Western Ghats Expedition, Satellite Triangulation, Public Dossiers |
| [🖼️ **Steganography & Misc**](#-steganography--misc) | **13** | Easy → Insane | 7-Stage Shattered QR Assembly, Trailing Whitespace, XOR Backups, Audio Spectrogram |
| [🤖 **AI & LLM Security**](#-ai--llm-security) | **1** | Medium | System Prompt Extraction, Persona Jailbreaking & Emotional Framing |
| **Total** | **69** | **All Tiers** | **Comprehensive Solution Archive** |

---

## 🏆 Featured Campaign Missions

Several challenges in ByteMeCTF were designed as progressive, multi-stage narratives:

### 🧩 1. The Soul Stone QR Series (7 Progressive Levels)
*Created by **Suyog Jadhav** ([Writeup Series](Writeups/suyog/MISC/soul_stone_qr_challenge_complete/SOUL_STONE_Shattered_Soul_Writeup.md))*
* An automated jigsaw puzzle where players reconstruct shattered QR code tiles with mathematical transformations.
* **Levels 0–6:** Ranging from $3 \times 3$ pure spatial shuffles to $10 \times 10$ grids with $90^\circ$ rotations, horizontal/vertical reflections, edge deletions, and decoy tiles.
* Features a full programmatic solver using OpenCV and border-pixel gradient scoring.

### 🧭 2. The Traveller's Trail OSINT Series (8 Sequential Stops)
*Created by **Sarthak Warale** ([Master Guide](Writeups/sarthak/OSINT/README.md))*
* A real-world geographic investigative trail following a traveller across the Western Ghats of Maharashtra:
  `Akurdi Station` ➔ `Kamshet` ➔ `Tikona Peth` ➔ `Vitandgad Fort` ➔ `Lohagad & Visapur` ➔ `Tung Fort & Pawna Lake` ➔ `Google Maps Digital Footprint` ➔ `Identity Reveal`.

### 🧠 3. Echoes of Vormir Memory Trail (6 Memory Stages)
*Created by **Sarthak Warale** ([Read Writeup](Writeups/sarthak/Forensics/echoes_of_vormir.md))*
* In-depth Volatility 3 analysis on a raw Windows memory dump (`Vormir.mem`): process mapping, VAD tree traversal, MS Paint artifact recovery, process memory carving, Edge browser tab recovery, and handles analysis.

### 🔗 4. Soul Fracture Relational Cryptography
*Created by **Suyog Jadhav** ([Read Writeup](Writeups/suyog/CRYPTO/soul_fracture.md))*
* 24 scrambled ciphertext fragments linked solely by echo-resonance properties.
* Solved by modeling the fragments as a directed graph, finding a Hamiltonian cycle via DFS backtracking, and deriving the key via 1337 rounds of SHA-256.

---

## 🌐 Web Exploitation

| Challenge | Difficulty | Author | Key Vulnerability / Concepts | Solution |
|---|:---:|---|---|:---:|
| **Signal Console** | Hard | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | SSTI in Jinja2, Sandboxed Environment Escape, Remote Code Execution | [Writeup →](Writeups/pratik/Web/signal_console.md) |
| **Soul Fragment Race** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Database Concurrency Race Condition, Ephemeral Token Recovery | [Writeup →](Writeups/pratik/Web/soul_fragment_race.md) |
| **Soul Split — The Third Guardian** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Parser Differential, Nginx vs. Flask Path Discrepancy, Route Smuggling | [Writeup →](Writeups/pratik/Web/soul_split.md) |
| **Soul Trial** | Medium | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Rate Limiting Bypass, Client Header Spoofing (`X-Forwarded-For`) | [Writeup →](Writeups/pratik/Web/soul_trial.md) |
| **Soul Archive** | Medium | [Aryan Bansode](AUTHORS.md#aryan-bansode) | SSRF via Quantum Relay, Internal Docker Vault, HMAC Chamber Ticket Flow | [Writeup →](Writeups/aryan/web/soul_stone.md) |
| **ReportHub** | Hard | [Aryan Bansode](AUTHORS.md#aryan-bansode) | Dynamic PDF Generator XSS, Local File Extraction via Headless Renderer | [Writeup →](Writeups/aryan/web/reporthub.md) |
| **ECHO//NULL** | Medium | [Aryan Havkar](AUTHORS.md#aryan-havkar) | Jinja2 SSTI, Context Introspection, Hidden Sector Mirror Flag | [Writeup →](Writeups/aryanhavkar23/Web/sqli-0.md) |
| **Split Session** | Medium | [Narendra Lomate](AUTHORS.md#narendra-lomate) | Flask Session Secret Key Extraction, Cookie Forgery & Privilege Escalation | [Writeup →](Writeups/narendra/Web/split_session.md) |
| **PWN-CTF: ASLR Breaker** | Easy | [Shreya Gaikwad](AUTHORS.md#shreya-gaikwad) | PHP Memory Information Leak, Remote Base Address Calculation | [Writeup →](Writeups/shreya/Web/aslr_breaker.md) |
| **ARCHIVE // 09** | Hard | [Shreya Gaikwad](AUTHORS.md#shreya-gaikwad) | Local File Inclusion (LFI), Path Traversal Filter Evasion | [Writeup →](Writeups/shreya/Web/archive_09.md) |
| **GradePortal - JWT Secret Reuse** | Hard | [Siddharth Kabade](AUTHORS.md#siddharth-kabade) | JWT Algorithm Confusion, Symmetric Secret Key Reuse across Services | [Writeup →](Writeups/siddharth/Web/gradeportal_jwt_secret_reuse.md) |
| **Collectors' Circle — Guestbook** | Medium | [Shivram Parkhi](AUTHORS.md#shivram-parkhi) | Stored Cross-Site Scripting (XSS), Admin Bot Cookie Theft | [Writeup →](Writeups/shivram/web/guestbook.md) |
| **Fractured Identity** | Medium | [Arpita Nikam](AUTHORS.md#arpita-nikam) | Insecure Direct Object Reference (IDOR), Broken Object-Level Authorization | [Writeup →](Writeups/arpita/Web/fractured_identity.md) |

---

## 💥 Pwn / Binary Exploitation

| Challenge | Difficulty | Author | Vulnerability & Architecture | Solution |
|---|:---:|---|---|:---:|
| **Soul // Memory of Thanos** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Format String Bug, Libc Leak, Global Offset Table (GOT) Overwrite | [Writeup →](Writeups/suyog/BINARY/soul_memory_of_thanos.md) |
| **Soul Vault: The Collector** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stack Canary Information Leak, 64-bit Return-Oriented Programming (ROP) | [Writeup →](Writeups/suyog/BINARY/soul_vault_collector.md) |
| **Soul's Weakness** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Classic Stack Buffer Overflow, Instruction Pointer Hijack, ret2win | [Writeup →](Writeups/suyog/BINARY/souls_weakness.md) |
| **House of Water** | Hard | [Om Khanjodkar](AUTHORS.md#om-khanjodkar) | Dynamic Heap Exploitation, House of Force, Top Chunk Misalignment | [Writeup →](Writeups/om/Pwn/house_of_water.md) |
| **Return to Win** | Easy | [Om Khanjodkar](AUTHORS.md#om-khanjodkar) | Unsafe `gets()` Call, Stack Smash, Non-PIE Return-to-Win Target | [Writeup →](Writeups/om/Pwn/return_to_win.md) |

---

## 🔓 Reverse Engineering & Mobile

| Challenge | Difficulty | Author | Architecture & Reverse Engineering Vector | Solution |
|---|:---:|---|---|:---:|
| **SoulVault (Android)** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Obfuscated Native JNI (`.so`), JADX Reflection, Native SHA-256 Proof of Work | [Writeup →](Writeups/pratik/Mobile/soulvault.md) |
| **Soul Ascension (Android)** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Android Native Decryption, Dynamic Runtime Hooking (Frida), Memory Patching | [Writeup →](Writeups/pratik/Mobile/soul_ascension.md) |
| **SoulVault (Linux VM)** | Insane | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stripped Custom Virtual Machine in Go, Bytecode Disassembler & Opcode Analysis | [Writeup →](Writeups/suyog/REVERSE/soulvault.md) |
| **SoulStone (Trial of Vormir)** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Multi-stage Key Scheduling Algorithm, Bijective Stream Cipher Inversion | [Writeup →](Writeups/suyog/REVERSE/soulstone.md) |
| **Soul Vault 0** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Custom 8-bit Stack VM, Opcode Reverse Engineering, State Verification | [Writeup →](Writeups/suyog/REVERSE/soul_vault_0.md) |
| **Soul Echoes** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Anti-Debugging Check (`ptrace`), Inline XOR Obfuscation, String Reconstruction | [Writeup →](Writeups/suyog/REVERSE/soul_echoes.md) |
| **Soul's Whisper** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stripped 64-bit ELF, Function Call Tracing (`ltrace`), String Comparison | [Writeup →](Writeups/suyog/REVERSE/souls_whisper.md) |

---

## 🔐 Cryptography

| Challenge | Difficulty | Author | Cryptosystem & Mathematical Vector | Solution |
|---|:---:|---|---|:---:|
| **Soul Fracture** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Hamiltonian Cycle on 24-Node Graph, 1337-Round SHA-256 KDF, Stream Cipher | [Writeup →](Writeups/suyog/CRYPTO/soul_fracture.md) |
| **Soul's Locked Message** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Affine Cipher Inversion, Modular Inverse Arithmetic, Frequency Analysis | [Writeup →](Writeups/suyog/CRYPTO/souls_locked_message.md) |
| **Two Locks** | Medium | [Narendra Lomate](AUTHORS.md#narendra-lomate) | RSA Common Modulus Attack, Extended Euclidean Algorithm, Private Key Recovery | [Writeup →](Writeups/narendra/Crypto/two_locks.md) |
| **Infinity Vault** | Medium | [Vedant Deore](AUTHORS.md#vedant-deore) | AES-CBC Initialization Vector (IV) Reuse, Cryptographic Bit-Flipping Attack | [Writeup →](Writeups/Vedant/Crypto/Infinity_Vault.md) |
| **The Forgotten Echo** | Medium | [Vedant Deore](AUTHORS.md#vedant-deore) | Elliptic Curve Cryptography (ECC), Baby-Step Giant-Step Discrete Logarithm | [Writeup →](Writeups/Vedant/Crypto/The_Forgotten_Echo.md) |
| **The Soul Stone: A Worthy Sacrifice** | Medium | [Krishna Kulkarni](AUTHORS.md#krishna-kulkarni) | Multi-layer Base64, Repeating-Key XOR Stream Decryption, Key Derivation | [Writeup →](Writeups/krishna/stego-cryto/sacrifice.md) |

---

## 🔍 Digital & Network Forensics

| Challenge | Difficulty | Author | Artifact / Investigation Vector | Solution |
|---|:---:|---|---|:---:|
| **The Soul in the Wire** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Covert Channels (DNS Timing, ICMP ID, TCP Reordering, UDP Packet Lengths) | [Writeup →](Writeups/suyog/FORENSICS/soul_in_the_wire.md) |
| **The Soul Stone Intercept** | Medium-Hard | [Ishaan Jog](AUTHORS.md#ishaan-jog) | TLS Session Key Decryption, Packet Stream Reconstruction, Pcap Forensics | [Writeup →](Writeups/ishaan/network_forensics/ByteMe_PCAP_Solution.md) |
| **Echoes of Vormir (Memory Trail)** | Hard | [Sarthak Warale](AUTHORS.md#sarthak-warale) | 6-Stage Volatility 3 Memory Forensics (`Vormir.mem`), VADs, Process Injections | [Writeup →](Writeups/sarthak/Forensics/echoes_of_vormir.md) |
| **Echoes of Vormir (PNG Chunks)** | Easy | [Praniti Gangad](AUTHORS.md#praniti-gangad) | ExifTool Metadata Extraction, Non-Standard PNG Chunk Analysis, Base64 Staging | [Writeup →](Writeups/praniti031-dotcom/Forensics/echoes-of-vormir.md) |
| **Thanos's Garden** | Medium | [Urvish Bharde](AUTHORS.md#urvish-bharde) | Disguised File Headers, LUKS Encrypted Disk Image, Contact Sheet Forensics | [Writeup →](Writeups/urvish/forensics/thanos_garden_writeup.md) |
| **Sacrifice** | Medium | [Urvish Bharde](AUTHORS.md#urvish-bharde) | Wireshark USB Capture Analysis, Audio Stream Filtering, Steghide Key Extraction | [Writeup →](Writeups/urvish/forensics/Sacrifice_writeup.md) |
| **The Keeper's Trail** | Hard | [Somay Rathod](AUTHORS.md#somay-rathod) | Damaged Archive Carving, Hex Inspection, Multi-archive Layer Reconstruction | [Writeup →](Writeups/Somay/Forensics/The-Keepers-Trail.md) |

---

## 🛰️ Open Source Intelligence (OSINT)

| Challenge | Difficulty | Author | Investigation Focus | Solution |
|---|:---:|---|---|:---:|
| **The Traveller's Trail (Master)** | Expert | [Sarthak Warale](AUTHORS.md#sarthak-warale) | 8-Part Sequential Journey Across Western Ghats (Pune ➔ Forts ➔ Identity) | [Master Guide →](Writeups/sarthak/OSINT/README.md) |
| ↳ *Traveller-1 : The First Stop* | Easy | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Suburban Railway Station Geolocation (Akurdi) | [Writeup →](Writeups/sarthak/OSINT/traveller_1.md) |
| ↳ *Traveller-2 : Seven Stops* | Easy | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Train Route Schedule & Station Counting (Kamshet) | [Writeup →](Writeups/sarthak/OSINT/traveller_2.md) |
| ↳ *Traveller-3 : The Road Ends Here* | Medium | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Local Bus Route & Base Village Triangulation (Tikona Peth) | [Writeup →](Writeups/sarthak/OSINT/traveller_3.md) |
| ↳ *Traveller-4 : Two Names, One Fort* | Medium | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Pyramid Peak Visual Match & Historical Fort Records (Vitandgad) | [Writeup →](Writeups/sarthak/OSINT/traveller_4.md) |
| ↳ *Traveller-5 : Two Shapes on the Horizon*| Hard | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Summit Sightline & Terrain Correlation (Lohagad & Visapur) | [Writeup →](Writeups/sarthak/OSINT/traveller_5.md) |
| ↳ *Traveller-6 : Across the Water* | Medium | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Lake Shoreline & Conical Bastion Matching (Tung Fort & Pawna Lake) | [Writeup →](Writeups/sarthak/OSINT/traveller_6.md) |
| ↳ *Traveller-7 : The Digital Footprint* | Hard | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Google Maps Review Mining (`glitchseeker`) & Base64 Metadata Extraction | [Writeup →](Writeups/sarthak/OSINT/traveller_7.md) |
| ↳ *Traveller-8 : Who Was the Traveller* | Expert | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Cross-Platform Identity Correlation (CTFtime & OWASP PCCOE Lead Dossier) | [Writeup →](Writeups/sarthak/OSINT/traveller_8.md) |
| **Stalker 0** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Image EXIF Metadata Parsing, Reverse Image Search, Geolocation | [Writeup →](Writeups/suyog/OSINT/stalker_0.md) |
| **Stalker 1** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Cross-Platform Username Enumeration, Social Profile Scraping | [Writeup →](Writeups/suyog/OSINT/stalker_1.md) |
| **Stalker 2** | Expert | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Corporate Registry Records, Public Land Records, Satellite Verification | [Writeup →](Writeups/suyog/OSINT/stalker_2.md) |
| **The Place** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Architectural Triangulation, Street View Correlation, Shadow Angles | [Writeup →](Writeups/suyog/OSINT/the_place.md) |
| **The Soul That Remained** | Medium | [Somay Rathod](AUTHORS.md#somay-rathod) | Monument Geolocation, Memorial Inscription Matching | [Writeup →](Writeups/Somay/OSINT/The-Soul-That-Remained.md) |
| **The Keeper's Legacy** | Medium | [Somay Rathod](AUTHORS.md#somay-rathod) | Astronomical Constellation Geolocation (Ursa Major / Pointer Stars) | [Writeup →](Writeups/Somay/OSINT/The-Keepers-Legacy.md) |
| **Red Skull's Trail** | Easy | [Hrishikesh](AUTHORS.md#hrishikesh-hrishi) | Visual Landmark Geolocation, Satellite Cross-Reference | [Writeup →](Writeups/Hrishi/OSINT/CTF1.md) |
| **Soul Stone's Legacy** | Easy | [Hrishikesh](AUTHORS.md#hrishikesh-hrishi) | Online Digital Presence, Footprint Analysis | [Writeup →](Writeups/Hrishi/OSINT/CF2.md) |
| **Souled Stone (VormirKeeper)** | Hard | [Shivram Parkhi](AUTHORS.md#shivram-parkhi) | Social Media Reconnaissance, Preikestolen Cliff Coordinates | [Writeup →](Writeups/shivram/osint/VormirKeeper.md) |

---

## 🖼️ Steganography & Misc

| Challenge | Difficulty | Author | Technique / Method | Solution |
|---|:---:|---|---|:---:|
| **SOUL STONE: Series Guide** | Easy → Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Master Architecture, QR Generator & Combinatorial Solver | [Overview →](Writeups/suyog/MISC/soul_stone_qr_challenge_complete/SOUL_STONE_Shattered_Soul_Writeup.md) |
| ↳ *Level 0 — First Fragment* | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $3 \times 3$ grid (9 pieces), pure position shuffle | [Writeup →](Writeups/suyog/MISC/mission/level_0_first_fragment.md) |
| ↳ *Level 1 — Shattered Memories* | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $4 \times 4$ grid (16 pieces), positional shuffle + $90^\circ$ rotations | [Writeup →](Writeups/suyog/MISC/mission/level_1_shattered_memories.md) |
| ↳ *Level 2 — False Souls* | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $5 \times 5$ grid (25 pieces), rotations + decoy pieces inserted | [Writeup →](Writeups/suyog/MISC/mission/level_2_false_souls.md) |
| ↳ *Level 3 — Lost Edge* | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $6 \times 6$ grid (36 pieces), edge boundary removal + rotations | [Writeup →](Writeups/suyog/MISC/mission/level_3_lost_edge.md) |
| ↳ *Level 4 — Judgment of Vormir*| Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $7 \times 7$ grid (49 pieces), gradient matching + false edge rejection | [Writeup →](Writeups/suyog/MISC/mission/level_4_judgment_of_vormir.md) |
| ↳ *Level 5 — Soul World* | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $8 \times 8$ grid (64 pieces), $90^\circ$ rotations + mirror flips + decoys | [Writeup →](Writeups/suyog/MISC/mission/level_5_soul_world.md) |
| ↳ *Level 6 — The Soul Stone* | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | $10 \times 10$ grid (100 pieces), full combinatorial transformation solver | [Writeup →](Writeups/suyog/MISC/mission/level_6_the_soul_stone.md) |
| **Sanity Check** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Community Discord Verification, Impostor Profile Detection, Flag Format Check | [Writeup →](Writeups/suyog/MISC/sanity_check.md) |
| **SoulStone Invisible Signal** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Audio Waveform Analysis, Spectrogram Inscription, LSB Decoding | [Writeup →](Writeups/suyog/STEGO/soulstone_invisible_signal.md) |
| **One Soul, One Truth** | Medium | [Oshin Shukla](AUTHORS.md#oshin-shukla-azurecurrent) | Spatial LSB Image Steganography, Color Plane Isolation | [Writeup →](Writeups/oshinshukla07/Steganography/one_soul_one_truth.md) |
| **The Fifth Stone** | Insane | [Oshin Shukla](AUTHORS.md#oshin-shukla-azurecurrent) | Steghide Passphrase Recovery, Palette Manipulation, Multi-Layer Embedding | [Writeup →](Writeups/oshinshukla07/Steganography/the_fifth_stone.md) |
| **Broken Backup** | Easy–Medium | [Swara Shirke](AUTHORS.md#swara-shirke) | Configuration Analysis, Decimal to Hex, Single-byte XOR Obfuscation | [Writeup →](Writeups/Swara/MISC/broken_backup.md) |
| **Stego_SoulStone** | Medium–Hard | [Swara Shirke](AUTHORS.md#swara-shirke) | Trailing Whitespace Covert Channel, Base64 Stream, Repeating-Key XOR | [Writeup →](Writeups/Swara/MISC/stego_soulstone.md) |

---

## 🤖 AI & LLM Security

| Challenge | Difficulty | Author | Attack Vector & Model Interaction | Solution |
|---|:---:|---|---|:---:|
| **Vormir's Keeper** | Medium | [Ishaan Jog](AUTHORS.md#ishaan-jog) | System Prompt Extraction, Persona Jailbreaking, Multi-turn Emotional Framing | [Writeup →](Writeups/ishaan/llm_jailbreak/LLM_SOLUTION.md) |

---

## 👥 Authors Directory

Special thanks to all **20 authors and challenge creators** from the OWASP PCCOE team:

| Author | Handle | Challenges Authored |
|---|---|---|
| **Suyog Jadhav** | [@suyog-jadhav](https://github.com/suyog-jadhav) | Binary Exploitation (3), Reverse Engineering (5), Crypto (2), Forensics (1), Misc/QR (8), OSINT (4) |
| **Sarthak Warale** | [@sarthak-warale](https://github.com/sarthak-warale) | The Traveller's Trail OSINT Series (9), Volatility 3 Memory Forensics (1) |
| **Pratik Jadhav** | [@Pratik8262](https://github.com/Pratik8262) | Web Exploitation (4), Android Reverse Engineering / JNI (2) |
| **Aryan Bansode** | [@aryanbansode](https://github.com/aryanbansode) | Web Exploitation: Soul Archive (SSRF) & ReportHub (PDF XSS) |
| **Ishaan Jog** | [@Ishaan-Jog](https://github.com/Ishaan-Jog) | AI LLM Jailbreaking: Vormir's Keeper, Network Forensics (TLS PCAP) |
| **Narendra Lomate** | [@narendralomate2006](https://github.com/narendralomate2006) | Web: Split Session (Flask), Crypto: Two Locks (RSA Common Modulus) |
| **Om Khanjodkar** | [@omkhanjodkar-dev](https://github.com/omkhanjodkar-dev) | Binary Exploitation: House of Water (Heap) & Return to Win (ret2win) |
| **Oshin Shukla (AzureCurrent)** | [@oshinshukla07](https://github.com/oshinshukla07) | Steganography: One Soul One Truth & The Fifth Stone |
| **Shreya Gaikwad** | [@shreya-gaikwad](https://github.com/shreya-gaikwad) | Web Exploitation: ASLR Breaker & ARCHIVE // 09 (LFI) |
| **Somay Rathod** | [@SomayRathod](https://github.com/SomayRathod) | Forensics: The Keeper's Trail, OSINT: The Soul That Remained & The Keeper's Legacy |
| **Shivram Parkhi** | [@Shivramamol](https://github.com/Shivramamol) | Web: Guestbook (Stored XSS), OSINT: Souled Stone (VormirKeeper) |
| **Hrishikesh (Hrishi)** | [@Hrishi30-debug](https://github.com/Hrishi30-debug) | OSINT: Red Skull's Trail & Soul Stone's Legacy |
| **Urvish Bharde** | [@Recursive_Error](https://github.com/Recursive_Error) | Forensics: Thanos's Garden (Encrypted Disk) & Sacrifice (Audio PCAP) |
| **Vedant Deore** | [@VedantDeore](https://github.com/VedantDeore) | Cryptography: Infinity Vault (AES-CBC IV Reuse) & The Forgotten Echo (ECC DLog) |
| **Arpita Nikam** | [@nikamarpita640](https://github.com/nikamarpita640) | Web Exploitation: Fractured Identity (IDOR / BOLA) |
| **Aryan Havkar** | [@aryanhavkar23](https://github.com/aryanhavkar23) | Web Exploitation: ECHO//NULL (SSTI Jinja2) |
| **Krishna Kulkarni** | [@krishna-kulkarni](https://github.com/krishna-kulkarni) | Cryptography: The Soul Stone: A Worthy Sacrifice (XOR Stream) |
| **Praniti Gangad** | [@praniti031-dotcom](https://github.com/praniti031-dotcom) | Digital Forensics: Echoes of Vormir (PNG Chunks & Exif) |
| **Siddharth Kabade** | [@siddharthkabade](https://github.com/siddharthkabade) | Web Exploitation: GradePortal (JWT Secret Reuse) |
| **Swara Shirke** | [@swaraops](https://github.com/swaraops) | Misc: Broken Backup (XOR) & Stego_SoulStone (Whitespace Stego) |

> 📖 *For detailed profiles, biographies, and full challenge catalogs, visit [AUTHORS.md](AUTHORS.md).*

---

## 📁 Repository Structure

```text
ByteMeCTF-WriteUps/
├── README.md               # Main repository showcase and participant portal
├── CATEGORY_INDEX.md       # Full category-by-category index with concepts & writeup links
├── AUTHORS.md              # Author roster, github handles, and categorized works
├── CONTRIBUTING.md         # Guidelines, conventions, and templates for contributors
├── .gitignore              # Repository gitignore rules
└── Writeups/               # Primary challenge writeup directories
    ├── <author-handle>/
    │   └── <Category>/
    │       ├── <challenge_name>.md
    │       ├── resources/
    │       │   ├── screenshot.png
    │       │   ├── solve.py
    │       │   └── artifact.pcap
    └── pratik/
        └── Word_Documents/ # Official styled .docx exports for offline study
```

---

## 💡 Information for Participants & Learners

* **Interactive Solvers:** Most writeups include functional Python solver scripts inline or inside the associated `resources/` folder.
* **Reproducibility:** Re-run exploits locally by referencing the provided target ports and docker configs where applicable.
* **Offline Reading:** For participants who prefer formatted document exports, pre-compiled Word documents are available in [Writeups/pratik/Word_Documents/](Writeups/pratik/Word_Documents/).
* **Questions / Feedback:** Found a typo or want to share alternative solve techniques? Open an [Issue](https://github.com/suyog-jadhav/ByteMeCTF-WriteUps/issues) or submit a Pull Request!

---

<div align="center">
  <sub>Built with ❤️ by the <b>OWASP PCCOE Student Chapter</b> for the cybersecurity community.</sub><br/>
  <sub>© 2026 ByteMeCTF. All rights reserved.</sub>
</div>
