# ByteMeCTF — Category Index

A categorized, searchable catalog of all official challenge solutions and writeups from **ByteMeCTF**, organized by domain and vulnerability type.

---

## ⚡ Quick Navigation

* [🌐 Web Exploitation](#-web-exploitation-13-challenges)
* [💥 Pwn / Binary Exploitation](#-pwn--binary-exploitation-5-challenges)
* [🔓 Reverse Engineering & Mobile](#-reverse-engineering--mobile-7-challenges)
* [🔐 Cryptography](#-cryptography-6-challenges)
* [🔍 Digital & Network Forensics](#-digital--network-forensics-7-challenges)
* [🛰️ Open Source Intelligence (OSINT)](#-open-source-intelligence-osint-18-challenges)
* [🖼️ Steganography & Misc](#-steganography--misc-11-challenges)
* [🤖 AI & LLM Security](#-ai--llm-security-1-challenge)

---

## 🌐 Web Exploitation (13 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Signal Console** | Hard | Pratik Jadhav | SSTI in Jinja2, Sandboxed Environment Escape, Remote Code Execution | [Read Writeup →](Writeups/pratik/Web/signal_console.md) |
| **Soul Fragment Race** | Expert | Pratik Jadhav | Concurrency Flaw, Database Race Condition, Ephemeral Token Recovery | [Read Writeup →](Writeups/pratik/Web/soul_fragment_race.md) |
| **Soul Split — The Third Guardian** | Expert | Pratik Jadhav | Parser Differential, Nginx vs. Flask Path Discrepancy, Route Smuggling | [Read Writeup →](Writeups/pratik/Web/soul_split.md) |
| **Soul Trial** | Medium | Pratik Jadhav | Rate Limiting Bypass, Client Header Spoofing (`X-Forwarded-For`) | [Read Writeup →](Writeups/pratik/Web/soul_trial.md) |
| **Soul Archive** | Medium | Aryan Bansode | Server-Side Request Forgery (SSRF), Relay Filtering Bypass, HMAC Session Flow | [Read Writeup →](Writeups/aryan/web/soul_stone.md) |
| **ReportHub** | Hard | Aryan Bansode | Dynamic PDF Generator XSS, Local File Extraction via Headless Renderer | [Read Writeup →](Writeups/aryan/web/reporthub.md) |
| **ECHO//NULL** | Medium | Aryan Havkar | Server-Side Template Injection (SSTI), Context Inspection, Diagnostic API | [Read Writeup →](Writeups/aryanhavkar23/Web/sqli-0.md) |
| **Split Session** | Medium | Narendra Lomate | Flask Session Secret Key Extraction, Cookie Forgery & Privilege Escalation | [Read Writeup →](Writeups/narendra/Web/split_session.md) |
| **PWN-CTF: ASLR Breaker** | Easy | Shreya Gaikwad | PHP Memory Information Leak, Remote Base Address Calculation | [Read Writeup →](Writeups/shreya/Web/aslr_breaker.md) |
| **ARCHIVE // 09** | Hard | Shreya Gaikwad | Local File Inclusion (LFI), URL Encoding Filter Evasion, Log Poisoning | [Read Writeup →](Writeups/shreya/Web/archive_09.md) |
| **GradePortal - JWT Secret Reuse** | Hard | Siddharth Kabade | JWT Algorithm Confusion, Symmetric Key Misuse across Microservices | [Read Writeup →](Writeups/siddharth/Web/gradeportal_jwt_secret_reuse.md) |
| **Collectors' Circle — Guestbook** | Medium | Shivram Parkhi | Stored Cross-Site Scripting (XSS), Simulated Admin Bot Cookie Theft | [Read Writeup →](Writeups/shivram/web/guestbook.md) |
| **Fractured Identity** | Medium | Arpita Nikam | Insecure Direct Object Reference (IDOR), Broken Object-Level Authorization | [Read Writeup →](Writeups/arpita/Web/fractured_identity.md) |

---

## 💥 Pwn / Binary Exploitation (5 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Soul // Memory of Thanos** | Hard | Suyog Jadhav | Format String Vulnerability, Global Offset Table (GOT) Overwrite, Libc Leak | [Read Writeup →](Writeups/suyog/BINARY/soul_memory_of_thanos.md) |
| **Soul Vault: The Collector** | Hard | Suyog Jadhav | Stack Canary Bypass via Information Leak, 64-bit Return-Oriented Programming (ROP) | [Read Writeup →](Writeups/suyog/BINARY/soul_vault_collector.md) |
| **Soul's Weakness** | Easy | Suyog Jadhav | Classic Stack Buffer Overflow, Instruction Pointer Control, Target Redirection | [Read Writeup →](Writeups/suyog/BINARY/souls_weakness.md) |
| **House of Water** | Hard | Om Khanjodkar | Dynamic Heap Exploitation, House of Force, Top Chunk Misalignment, Target Write | [Read Writeup →](Writeups/om/Pwn/house_of_water.md) |
| **Return to Win** | Easy | Om Khanjodkar | Unsafe `gets()` Call, Stack Smash, Non-PIE Return-to-Win Execution | [Read Writeup →](Writeups/om/Pwn/return_to_win.md) |

---

## 🔓 Reverse Engineering & Mobile (7 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Architecture | Writeup |
|---|:---:|---|---|:---:|
| **SoulVault (Mobile)** | Expert | Pratik Jadhav | Android APK, Obfuscated Native JNI (`.so`), JADX, Native Reflection & Proof of Work | [Read Writeup →](Writeups/pratik/Mobile/soulvault.md) |
| **Soul Ascension (Mobile)** | Expert | Pratik Jadhav | Android Native Decryption, Dynamic Runtime Hooking (Frida), Memory Patching | [Read Writeup →](Writeups/pratik/Mobile/soul_ascension.md) |
| **SoulVault (Linux VM)** | Insane | Suyog Jadhav | Stripped Custom Virtual Machine, Bytecode Disassembly, Opcode Dispatch Architecture | [Read Writeup →](Writeups/suyog/REVERSE/soulvault.md) |
| **SoulStone (Trial of Vormir)** | Hard | Suyog Jadhav | Multi-stage Key Scheduling Algorithm, Bijective Stream Cipher Inversion | [Read Writeup →](Writeups/suyog/REVERSE/soulstone.md) |
| **Soul Vault 0** | Medium | Suyog Jadhav | Custom 8-bit Stack VM, Opcode Extraction, State Machine Reverse Engineering | [Read Writeup →](Writeups/suyog/REVERSE/soul_vault_0.md) |
| **Soul Echoes** | Easy | Suyog Jadhav | Anti-Debugging Check (`ptrace`), Inline XOR Obfuscation, String Reconstruction | [Read Writeup →](Writeups/suyog/REVERSE/soul_echoes.md) |
| **Soul's Whisper** | Easy | Suyog Jadhav | Stripped 64-bit ELF, Function Call Tracing (`ltrace`), Logic Recovery | [Read Writeup →](Writeups/suyog/REVERSE/souls_whisper.md) |

> 📁 *Source code, Dockerfiles, generators, and solver scripts are available under [Writeups/suyog/REVERSE/rev/](Writeups/suyog/REVERSE/rev/).*

---

## 🔐 Cryptography (6 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Cryptosystem | Writeup |
|---|:---:|---|---|:---:|
| **Soul Fracture** | Hard | Suyog Jadhav | Hamiltonian Cycle on 24-Node Graph, 1337-Round SHA-256 KDF, Custom Block Cipher | [Read Writeup →](Writeups/suyog/CRYPTO/soul_fracture.md) |
| **Soul's Locked Message** | Medium | Suyog Jadhav | Affine Cipher Inversion, Modular Inverse Arithmetic, Frequency Analysis | [Read Writeup →](Writeups/suyog/CRYPTO/souls_locked_message.md) |
| **Two Locks** | Medium | Narendra Lomate | RSA Common Modulus Attack, Extended Euclidean Algorithm, Private Key Recovery | [Read Writeup →](Writeups/narendra/Crypto/two_locks.md) |
| **Infinity Vault** | Medium | Vedant Deore | AES-CBC Initialization Vector (IV) Reuse, Cryptographic Bit-Flipping Attack | [Read Writeup →](Writeups/Vedant/Crypto/Infinity_Vault.md) |
| **The Forgotten Echo** | Medium | Vedant Deore | Elliptic Curve Cryptography (ECC), Pohlig-Hellman / Baby-Step Giant-Step DLog | [Read Writeup →](Writeups/Vedant/Crypto/The_Forgotten_Echo.md) |
| **The Soul Stone: A Worthy Sacrifice** | Medium | Krishna Kulkarni | Multi-layer Base64, Repeating-Key XOR Stream Decryption, Key Derivation | [Read Writeup →](Writeups/krishna/stego-cryto/sacrifice.md) |

---

## 🔍 Digital & Network Forensics (7 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Forensic Artifact | Writeup |
|---|:---:|---|---|:---:|
| **The Soul in the Wire** | Hard | Suyog Jadhav | Covert Network Channels (DNS Timing, ICMP ID, TCP Reordering, UDP Lengths) | [Read Writeup →](Writeups/suyog/FORENSICS/soul_in_the_wire.md) |
| **The Soul Stone Intercept** | Medium-Hard | Ishaan Jog | Network Traffic Analysis, TLS Session Key Decryption, Packet Stream Reconstruction | [Read Writeup →](Writeups/ishaan/network_forensics/ByteMe_PCAP_Solution.md) |
| **Echoes of Vormir: The Memory Trail** | Hard | Sarthak Warale | 6-Stage Volatility 3 Memory Dump Forensics (`Vormir.mem`), Process Carving, Browser Cache | [Read Writeup →](Writeups/sarthak/Forensics/echoes_of_vormir.md) |
| **Echoes of Vormir (PNG Chunks)** | Easy | Praniti Gangad | ExifTool Metadata Extraction, Non-Standard PNG Chunk Analysis, Base64 Reconstruction | [Read Writeup →](Writeups/praniti031-dotcom/Forensics/echoes-of-vormir.md) |
| **Thanos's Garden** | Medium | Urvish Bharde | Disguised File Headers, LUKS Encrypted Disk Image, Contact Sheet EXIF Inspection | [Read Writeup →](Writeups/urvish/forensics/thanos_garden_writeup.md) |
| **Sacrifice** | Medium | Urvish Bharde | Wireshark USB Capture Analysis, Audio Stream Filtering, Steghide Key Extraction | [Read Writeup →](Writeups/urvish/forensics/Sacrifice_writeup.md) |
| **The Keeper's Trail** | Hard | Somay Rathod | Damaged Archive Carving, Hex Inspection, Multi-archive Layer Reconstruction | [Read Writeup →](Writeups/Somay/Forensics/The-Keepers-Trail.md) |

---

## 🛰️ Open Source Intelligence (OSINT) (18 Challenges)

### 🏔️ The Traveller's Trail Campaign (8-Part Series by Sarthak Warale)
*A continuous, multi-stage expedition reconstructing an investigator's route through the Western Ghats:*

| Stage | Challenge Name | Difficulty | Location / Target | Writeup |
|:---:|---|:---:|---|:---:|
| **Overview** | **The Traveller's Trail (Master Guide)** | Expert | Full Expedition Map & Summary | [Read Guide →](Writeups/sarthak/OSINT/README.md) |
| **1** | Traveller-1 : The First Stop | Easy | Akurdi Railway Station Identification | [Read Writeup →](Writeups/sarthak/OSINT/traveller_1.md) |
| **2** | Traveller-2 : Seven Stops | Easy | Pune–Lonavala Train Timetable & Station Counting (Kamshet) | [Read Writeup →](Writeups/sarthak/OSINT/traveller_2.md) |
| **3** | Traveller-3 : The Road Ends Here | Medium | Local Bus Route & Base Village Triangulation (Tikona Peth) | [Read Writeup →](Writeups/sarthak/OSINT/traveller_3.md) |
| **4** | Traveller-4 : Two Names, One Fort | Medium | Pyramid Peak Visual Match & Historical Record (Vitandgad) | [Read Writeup →](Writeups/sarthak/OSINT/traveller_4.md) |
| **5** | Traveller-5 : Two Shapes on the Horizon | Hard | Ridge Sightline Analysis & Twin Fort Identification (Lohagad / Visapur) | [Read Writeup →](Writeups/sarthak/OSINT/traveller_5.md) |
| **6** | Traveller-6 : Across the Water | Medium | Reservoir Shoreline & Conical Bastion Matching (Tung & Pawna Lake) | [Read Writeup →](Writeups/sarthak/OSINT/traveller_6.md) |
| **7** | Traveller-7 : The Digital Footprint | Hard | Google Maps Review Profiling (`glitchseeker`) & Base64 Metadata | [Read Writeup →](Writeups/sarthak/OSINT/traveller_7.md) |
| **8** | Traveller-8 : Who Was the Traveller | Expert | Identity Correlation, CTFtime User Mapping, Team Lead Dossier | [Read Writeup →](Writeups/sarthak/OSINT/traveller_8.md) |

### 🌐 Standalone OSINT Challenges
| Challenge | Difficulty | Author | Objective / Methodology | Writeup |
|---|:---:|---|---|:---:|
| **Stalker 0** | Easy | Suyog Jadhav | Image EXIF Metadata Parsing, Reverse Image Search, Geolocation | [Read Writeup →](Writeups/suyog/OSINT/stalker_0.md) |
| **Stalker 1** | Medium | Suyog Jadhav | Cross-Platform Username Enumeration, Social Profile Scraping, Handle Tracing | [Read Writeup →](Writeups/suyog/OSINT/stalker_1.md) |
| **Stalker 2** | Expert | Suyog Jadhav | Corporate Registry Records, Public Land Records, Satellite Verification | [Read Writeup →](Writeups/suyog/OSINT/stalker_2.md) |
| **The Place** | Medium | Suyog Jadhav | Architectural Triangulation, Street View Correlation, Shadow Angles | [Read Writeup →](Writeups/suyog/OSINT/the_place.md) |
| **The Soul That Remained** | Medium | Somay Rathod | Monument Geolocation, Memorial Inscription Matching | [Read Writeup →](Writeups/Somay/OSINT/The-Soul-That-Remained.md) |
| **The Keeper's Legacy** | Medium | Somay Rathod | Astronomical Constellation Geolocation (Ursa Major / Big Dipper Pointer Stars) | [Read Writeup →](Writeups/Somay/OSINT/The-Keepers-Legacy.md) |
| **Red Skull's Trail** | Easy | Hrishikesh (Hrishi) | Visual Landmark Geolocation, Satellite Cross-Reference | [Read Writeup →](Writeups/Hrishi/OSINT/CTF1.md) |
| **Soul Stone's Legacy** | Easy | Hrishikesh (Hrishi) | Online Digital Presence, Footprint Analysis | [Read Writeup →](Writeups/Hrishi/OSINT/CF2.md) |
| **Souled Stone (VormirKeeper)** | Hard | Shivram Parkhi | Social Media Account Reconnaissance, Preikestolen Cliff Coordinates | [Read Writeup →](Writeups/shivram/osint/VormirKeeper.md) |

---

## 🖼️ Steganography & Misc (11 Challenges)

### 🧩 The Soul Stone QR Series (7 Progressive Levels by Suyog Jadhav)
*A progressive puzzle reconstructing shattered QR codes using automated image edge matching, rotation alignment, and decoy rejection:*

| Level | Name | Difficulty | Grid & Mechanics | Writeup |
|:---:|---|:---:|---|:---:|
| **—** | **SOUL STONE: Complete Guide** | Easy → Hard | Architectural Overview, Generator & Master Solver Script | [Read Overview →](Writeups/suyog/MISC/soul_stone_qr_challenge_complete/SOUL_STONE_Shattered_Soul_Writeup.md) |
| **0** | Level 0 — First Fragment | Easy | $3 \times 3$ grid (9 pieces), pure position shuffle | [Read Writeup →](Writeups/suyog/MISC/mission/level_0_first_fragment.md) |
| **1** | Level 1 — Shattered Memories | Easy | $4 \times 4$ grid (16 pieces), positional shuffle + $90^\circ$ rotations | [Read Writeup →](Writeups/suyog/MISC/mission/level_1_shattered_memories.md) |
| **2** | Level 2 — False Souls | Medium | $5 \times 5$ grid (25 pieces), rotations + decoy pieces inserted | [Read Writeup →](Writeups/suyog/MISC/mission/level_2_false_souls.md) |
| **3** | Level 3 — Lost Edge | Medium | $6 \times 6$ grid (36 pieces), edge boundary removal + rotations | [Read Writeup →](Writeups/suyog/MISC/mission/level_3_lost_edge.md) |
| **4** | Level 4 — Judgment of Vormir | Hard | $7 \times 7$ grid (49 pieces), gradient matching + false edge rejection | [Read Writeup →](Writeups/suyog/MISC/mission/level_4_judgment_of_vormir.md) |
| **5** | Level 5 — Soul World | Hard | $8 \times 8$ grid (64 pieces), $90^\circ$ rotations + mirror flips + decoys | [Read Writeup →](Writeups/suyog/MISC/mission/level_5_soul_world.md) |
| **6** | Level 6 — The Soul Stone | Hard | $10 \times 10$ grid (100 pieces), full combinatorial transformation solver | [Read Writeup →](Writeups/suyog/MISC/mission/level_6_the_soul_stone.md) |

### 🎨 Standalone Steganography & Misc Challenges
| Challenge | Difficulty | Author | Technique / Method | Writeup |
|---|:---:|---|---|:---:|
| **Sanity Check** | Easy | Suyog Jadhav | Community Discord Verification, Impostor Channel Detection, Flag Format Check | [Read Writeup →](Writeups/suyog/MISC/sanity_check.md) |
| **SoulStone Invisible Signal** | Medium | Suyog Jadhav | Audio Waveform Analysis, High-Frequency Spectrogram Inscription, LSB Decoding | [Read Writeup →](Writeups/suyog/STEGO/soulstone_invisible_signal.md) |
| **One Soul, One Truth** | Medium | Oshin Shukla (AzureCurrent) | Spatial LSB Image Steganography, Color Plane Isolation | [Read Writeup →](Writeups/oshinshukla07/Steganography/one_soul_one_truth.md) |
| **The Fifth Stone** | Insane | Oshin Shukla (AzureCurrent) | Steghide Passphrase Recovery, Palette Manipulation, Multi-Layer Embedding | [Read Writeup →](Writeups/oshinshukla07/Steganography/the_fifth_stone.md) |
| **Broken Backup** | Easy–Medium | Swara Shirke | Configuration Analysis, Decimal to Hex, XOR Obfuscation | [Read Writeup →](Writeups/Swara/MISC/broken_backup.md) |
| **Stego_SoulStone** | Medium–Hard | Swara Shirke | Trailing Whitespace Stego, Base64 Stream, Repeating-Key XOR | [Read Writeup →](Writeups/Swara/MISC/stego_soulstone.md) |

---

## 🤖 AI & LLM Security (1 Challenge)

| Challenge | Difficulty | Author | Primary Concept / Attack Vector | Writeup |
|---|:---:|---|---|:---:|
| **Vormir's Keeper** | Medium | Ishaan Jog | System Prompt Extraction, Persona Jailbreaking, Multi-turn Emotional Framing | [Read Writeup →](Writeups/ishaan/llm_jailbreak/LLM_SOLUTION.md) |
