# ByteMeCTF - Category Index

A categorized, searchable catalog of all official challenge solutions and writeups from ByteMeCTF, sorted by difficulty level under each domain.

---

## Quick Navigation

* [Web Exploitation](#web-exploitation-13-challenges)
* [Pwn / Binary Exploitation](#pwn--binary-exploitation-5-challenges)
* [Reverse Engineering & Mobile](#reverse-engineering--mobile-7-challenges)
* [Cryptography](#cryptography-6-challenges)
* [Digital & Network Forensics](#digital--network-forensics-7-challenges)
* [Open Source Intelligence (OSINT)](#open-source-intelligence-osint-18-challenges)
* [Steganography & Misc](#steganography--misc-13-challenges)
* [AI & LLM Security](#ai--llm-security-1-challenge)

---

## Web Exploitation (13 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **PWN-CTF: ASLR Breaker** | Easy | [Shreya Gaikwad](AUTHORS.md#shreya-gaikwad) | PHP Memory Information Leak, Remote Base Address Calculation | [Read Writeup ->](Writeups/shreya/Web/aslr_breaker.md) |
| **ECHO//NULL** | Medium | [Aryan Havkar](AUTHORS.md#aryan-havkar) | Jinja2 SSTI, Context Introspection, Diagnostic API Reflection | [Read Writeup ->](Writeups/aryanhavkar23/Web/sqli-0.md) |
| **Fractured Identity** | Medium | [Arpita Nikam](AUTHORS.md#arpita-nikam) | Insecure Direct Object Reference (IDOR), Broken Object-Level Authorization | [Read Writeup ->](Writeups/arpita/Web/fractured_identity.md) |
| **Soul Archive** | Medium | [Aryan Bansode](AUTHORS.md#aryan-bansode) | SSRF via Quantum Relay, Internal Docker Vault, HMAC Chamber Ticket Flow | [Read Writeup ->](Writeups/aryan/web/soul_stone.md) |
| **Soul Trial** | Medium | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Rate Limiting Bypass, Client Header Spoofing (X-Forwarded-For) | [Read Writeup ->](Writeups/pratik/Web/soul_trial.md) |
| **Split Session** | Medium | [Narendra Lomate](AUTHORS.md#narendra-lomate) | Flask Session Secret Key Extraction, Cookie Forgery & Privilege Escalation | [Read Writeup ->](Writeups/narendra/Web/split_session.md) |
| **Collectors' Circle - Guestbook** | Medium | [Shivram Parkhi](AUTHORS.md#shivram-parkhi) | Stored Cross-Site Scripting (XSS), Admin Bot Cookie Theft | [Read Writeup ->](Writeups/shivram/web/guestbook.md) |
| **ARCHIVE // 09** | Hard | [Shreya Gaikwad](AUTHORS.md#shreya-gaikwad) | Local File Inclusion (LFI), Path Traversal Filter Evasion | [Read Writeup ->](Writeups/shreya/Web/archive_09.md) |
| **GradePortal - JWT Secret Reuse** | Hard | [Siddharth Kabade](AUTHORS.md#siddharth-kabade) | JWT Algorithm Confusion, Symmetric Secret Key Reuse across Services | [Read Writeup ->](Writeups/siddharth/Web/gradeportal_jwt_secret_reuse.md) |
| **ReportHub** | Hard | [Aryan Bansode](AUTHORS.md#aryan-bansode) | Dynamic PDF Generator XSS, Local File Extraction via Headless Renderer | [Read Writeup ->](Writeups/aryan/web/reporthub.md) |
| **Signal Console** | Hard | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | SSTI in Jinja2, Sandboxed Environment Escape, Remote Code Execution | [Read Writeup ->](Writeups/pratik/Web/signal_console.md) |
| **Soul Fragment Race** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Database Concurrency Race Condition, Ephemeral Token Recovery | [Read Writeup ->](Writeups/pratik/Web/soul_fragment_race.md) |
| **Soul Split - The Third Guardian** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Parser Differential, Nginx vs. Flask Path Discrepancy, Route Smuggling | [Read Writeup ->](Writeups/pratik/Web/soul_split.md) |


---

## Pwn / Binary Exploitation (5 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Return to Win** | Easy | [Om Khanjodkar](AUTHORS.md#om-khanjodkar) | Unsafe gets() Call, Stack Smash, Non-PIE Return-to-Win Target | [Read Writeup ->](Writeups/om/Pwn/return_to_win.md) |
| **Soul's Weakness** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Classic Stack Buffer Overflow, Instruction Pointer Hijack, ret2win | [Read Writeup ->](Writeups/suyog/BINARY/souls_weakness.md) |
| **House of Water** | Hard | [Om Khanjodkar](AUTHORS.md#om-khanjodkar) | Dynamic Heap Exploitation, House of Force, Top Chunk Misalignment | [Read Writeup ->](Writeups/om/Pwn/house_of_water.md) |
| **Soul // Memory of Thanos** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Format String Bug, Libc Leak, Global Offset Table (GOT) Overwrite | [Read Writeup ->](Writeups/suyog/BINARY/soul_memory_of_thanos.md) |
| **Soul Vault: The Collector** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stack Canary Information Leak, 64-bit Return-Oriented Programming (ROP) | [Read Writeup ->](Writeups/suyog/BINARY/soul_vault_collector.md) |


---

## Reverse Engineering & Mobile (7 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Soul Echoes** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Anti-Debugging Check (ptrace), Inline XOR Obfuscation, String Reconstruction | [Read Writeup ->](Writeups/suyog/REVERSE/soul_echoes.md) |
| **Soul's Whisper** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stripped 64-bit ELF, Function Call Tracing (ltrace), String Comparison | [Read Writeup ->](Writeups/suyog/REVERSE/souls_whisper.md) |
| **Soul Vault 0** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Custom 8-bit Stack VM, Opcode Reverse Engineering, State Verification | [Read Writeup ->](Writeups/suyog/REVERSE/soul_vault_0.md) |
| **SoulStone (Trial of Vormir)** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Multi-stage Key Scheduling Algorithm, Bijective Stream Cipher Inversion | [Read Writeup ->](Writeups/suyog/REVERSE/soulstone.md) |
| **Soul Ascension (Android)** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Android Native Decryption, Dynamic Runtime Hooking (Frida), Memory Patching | [Read Writeup ->](Writeups/pratik/Mobile/soul_ascension.md) |
| **SoulVault (Android)** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Obfuscated Native JNI (.so), JADX Reflection, Native SHA-256 Proof of Work | [Read Writeup ->](Writeups/pratik/Mobile/soulvault.md) |
| **SoulVault (Linux VM)** | Insane | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stripped Custom Virtual Machine in Go, Bytecode Disassembler & Opcode Analysis | [Read Writeup ->](Writeups/suyog/REVERSE/soulvault.md) |

> Source code, Dockerfiles, generators, and solver scripts are available under [Writeups/suyog/REVERSE/rev/](Writeups/suyog/REVERSE/rev/).


---

## Cryptography (6 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Infinity Vault** | Medium | [Vedant Deore](AUTHORS.md#vedant-deore) | AES-CBC Initialization Vector (IV) Reuse, Cryptographic Bit-Flipping Attack | [Read Writeup ->](Writeups/Vedant/Crypto/Infinity_Vault.md) |
| **Soul's Locked Message** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Affine Cipher Inversion, Modular Inverse Arithmetic, Frequency Analysis | [Read Writeup ->](Writeups/suyog/CRYPTO/souls_locked_message.md) |
| **The Forgotten Echo** | Medium | [Vedant Deore](AUTHORS.md#vedant-deore) | Elliptic Curve Cryptography (ECC), Baby-Step Giant-Step Discrete Logarithm | [Read Writeup ->](Writeups/Vedant/Crypto/The_Forgotten_Echo.md) |
| **The Soul Stone: A Worthy Sacrifice** | Medium | [Krishna Kulkarni](AUTHORS.md#krishna-kulkarni) | Multi-layer Base64, Repeating-Key XOR Stream Decryption, Key Derivation | [Read Writeup ->](Writeups/krishna/stego-cryto/sacrifice.md) |
| **Two Locks** | Medium | [Narendra Lomate](AUTHORS.md#narendra-lomate) | RSA Common Modulus Attack, Extended Euclidean Algorithm, Private Key Recovery | [Read Writeup ->](Writeups/narendra/Crypto/two_locks.md) |
| **Soul Fracture** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Hamiltonian Cycle on 24-Node Graph, 1337-Round SHA-256 KDF, Stream Cipher | [Read Writeup ->](Writeups/suyog/CRYPTO/soul_fracture.md) |


---

## Digital & Network Forensics (7 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Echoes of Vormir (PNG Chunks)** | Easy | [Praniti Gangad](AUTHORS.md#praniti-gangad) | ExifTool Metadata Extraction, Non-Standard PNG Chunk Analysis, Base64 Staging | [Read Writeup ->](Writeups/praniti031-dotcom/Forensics/echoes-of-vormir.md) |
| **Sacrifice** | Medium | [Urvish Bharde](AUTHORS.md#urvish-bharde) | Wireshark USB Capture Analysis, Audio Stream Filtering, Steghide Key Extraction | [Read Writeup ->](Writeups/urvish/forensics/Sacrifice_writeup.md) |
| **Thanos's Garden** | Medium | [Urvish Bharde](AUTHORS.md#urvish-bharde) | Disguised File Headers, LUKS Encrypted Disk Image, Contact Sheet Forensics | [Read Writeup ->](Writeups/urvish/forensics/thanos_garden_writeup.md) |
| **The Soul Stone Intercept** | Medium-Hard | [Ishaan Jog](AUTHORS.md#ishaan-jog) | TLS Session Key Decryption, Packet Stream Reconstruction, Pcap Forensics | [Read Writeup ->](Writeups/ishaan/network_forensics/ByteMe_PCAP_Solution.md) |
| **Echoes of Vormir (Memory Trail)** | Hard | [Sarthak Warale](AUTHORS.md#sarthak-warale) | 6-Stage Volatility 3 Memory Forensics (Vormir.mem), VADs, Process Injections | [Read Writeup ->](Writeups/sarthak/Forensics/echoes_of_vormir.md) |
| **The Keeper's Trail** | Hard | [Somay Rathod](AUTHORS.md#somay-rathod) | Damaged Archive Carving, Hex Inspection, Multi-archive Layer Reconstruction | [Read Writeup ->](Writeups/Somay/Forensics/The-Keepers-Trail.md) |
| **The Soul in the Wire** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Covert Channels (DNS Timing, ICMP ID, TCP Reordering, UDP Packet Lengths) | [Read Writeup ->](Writeups/suyog/FORENSICS/soul_in_the_wire.md) |


---

## Open Source Intelligence (OSINT) (18 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Red Skull's Trail** | Easy | [Hrishikesh (Hrishi)](AUTHORS.md#hrishikesh-hrishi) | Visual Landmark Geolocation, Satellite Cross-Reference | [Read Writeup ->](Writeups/Hrishi/OSINT/CTF1.md) |
| **Soul Stone's Legacy** | Easy | [Hrishikesh (Hrishi)](AUTHORS.md#hrishikesh-hrishi) | Online Digital Presence, Footprint Analysis | [Read Writeup ->](Writeups/Hrishi/OSINT/CF2.md) |
| **Stalker 0** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Image EXIF Metadata Parsing, Reverse Image Search, Geolocation | [Read Writeup ->](Writeups/suyog/OSINT/stalker_0.md) |
| **Traveller-1 : The First Stop** | Easy | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Suburban Railway Station Geolocation (Akurdi) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_1.md) |
| **Traveller-2 : Seven Stops** | Easy | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Train Route Schedule & Station Counting (Kamshet) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_2.md) |
| **Stalker 1** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Cross-Platform Username Enumeration, Social Profile Scraping | [Read Writeup ->](Writeups/suyog/OSINT/stalker_1.md) |
| **The Keeper's Legacy** | Medium | [Somay Rathod](AUTHORS.md#somay-rathod) | Astronomical Constellation Geolocation (Ursa Major / Pointer Stars) | [Read Writeup ->](Writeups/Somay/OSINT/The-Keepers-Legacy.md) |
| **The Place** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Architectural Triangulation, Street View Correlation, Shadow Angles | [Read Writeup ->](Writeups/suyog/OSINT/the_place.md) |
| **The Soul That Remained** | Medium | [Somay Rathod](AUTHORS.md#somay-rathod) | Monument Geolocation, Memorial Inscription Matching | [Read Writeup ->](Writeups/Somay/OSINT/The-Soul-That-Remained.md) |
| **Traveller-3 : The Road Ends Here** | Medium | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Local Bus Route & Base Village Triangulation (Tikona Peth) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_3.md) |
| **Traveller-4 : Two Names, One Fort** | Medium | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Pyramid Peak Visual Match & Historical Fort Records (Vitandgad) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_4.md) |
| **Traveller-6 : Across the Water** | Medium | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Lake Shoreline & Conical Bastion Matching (Tung Fort & Pawna Lake) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_6.md) |
| **Souled Stone (VormirKeeper)** | Hard | [Shivram Parkhi](AUTHORS.md#shivram-parkhi) | Social Media Reconnaissance, Preikestolen Cliff Coordinates | [Read Writeup ->](Writeups/shivram/osint/VormirKeeper.md) |
| **Traveller-5 : Two Shapes on the Horizon** | Hard | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Summit Sightline & Terrain Correlation (Lohagad & Visapur) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_5.md) |
| **Traveller-7 : The Digital Footprint** | Hard | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Google Maps Review Mining (glitchseeker) & Base64 Metadata Extraction | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_7.md) |
| **Stalker 2** | Expert | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Corporate Registry Records, Public Land Records, Satellite Verification | [Read Writeup ->](Writeups/suyog/OSINT/stalker_2.md) |
| **The Traveller's Trail (Master Guide)** | Expert | [Sarthak Warale](AUTHORS.md#sarthak-warale) | 8-Part Sequential Journey Across Western Ghats (Pune -> Forts -> Identity) | [Read Writeup ->](Writeups/sarthak/OSINT/README.md) |
| **Traveller-8 : Who Was the Traveller** | Expert | [Sarthak Warale](AUTHORS.md#sarthak-warale) | Cross-Platform Identity Correlation (CTFtime & Team Dossier) | [Read Writeup ->](Writeups/sarthak/OSINT/traveller_8.md) |


---

## Steganography & Misc (13 Challenges)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Sanity Check** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Community Discord Verification, Impostor Profile Detection, Flag Format Check | [Read Writeup ->](Writeups/suyog/MISC/sanity_check.md) |
| **Level 0 - First Fragment** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 3x3 grid (9 pieces), pure position shuffle | [Read Writeup ->](Writeups/suyog/MISC/mission/level_0_first_fragment.md) |
| **Level 1 - Shattered Memories** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 4x4 grid (16 pieces), positional shuffle + 90deg rotations | [Read Writeup ->](Writeups/suyog/MISC/mission/level_1_shattered_memories.md) |
| **Broken Backup** | Easy-Medium | [Swara Shirke](AUTHORS.md#swara-shirke) | Configuration Analysis, Decimal to Hex, Single-byte XOR Obfuscation | [Read Writeup ->](Writeups/Swara/MISC/broken_backup.md) |
| **Level 2 - False Souls** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 5x5 grid (25 pieces), rotations + decoy pieces inserted | [Read Writeup ->](Writeups/suyog/MISC/mission/level_2_false_souls.md) |
| **Level 3 - Lost Edge** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 6x6 grid (36 pieces), edge boundary removal + rotations | [Read Writeup ->](Writeups/suyog/MISC/mission/level_3_lost_edge.md) |
| **One Soul, One Truth** | Medium | [Oshin Shukla](AUTHORS.md#oshin-shukla-azurecurrent) | Spatial LSB Image Steganography, Color Plane Isolation | [Read Writeup ->](Writeups/oshinshukla07/Steganography/one_soul_one_truth.md) |
| **SoulStone Invisible Signal** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Audio Waveform Analysis, Spectrogram Inscription, LSB Decoding | [Read Writeup ->](Writeups/suyog/STEGO/soulstone_invisible_signal.md) |
| **Stego_SoulStone** | Medium-Hard | [Swara Shirke](AUTHORS.md#swara-shirke) | Trailing Whitespace Covert Channel, Base64 Stream, Repeating-Key XOR | [Read Writeup ->](Writeups/Swara/MISC/stego_soulstone.md) |
| **Level 4 - Judgment of Vormir** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 7x7 grid (49 pieces), gradient matching + false edge rejection | [Read Writeup ->](Writeups/suyog/MISC/mission/level_4_judgment_of_vormir.md) |
| **Level 5 - Soul World** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 8x8 grid (64 pieces), 90deg rotations + mirror flips + decoys | [Read Writeup ->](Writeups/suyog/MISC/mission/level_5_soul_world.md) |
| **Level 6 - The Soul Stone** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | 10x10 grid (100 pieces), full combinatorial transformation solver | [Read Writeup ->](Writeups/suyog/MISC/mission/level_6_the_soul_stone.md) |
| **The Fifth Stone** | Insane | [Oshin Shukla](AUTHORS.md#oshin-shukla-azurecurrent) | Steghide Passphrase Recovery, Palette Manipulation, Multi-Layer Embedding | [Read Writeup ->](Writeups/oshinshukla07/Steganography/the_fifth_stone.md) |


---

## AI & LLM Security (1 Challenge)

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Vormir's Keeper** | Medium | [Ishaan Jog](AUTHORS.md#ishaan-jog) | System Prompt Extraction, Persona Jailbreaking, Multi-turn Emotional Framing | [Read Writeup ->](Writeups/ishaan/llm_jailbreak/LLM_SOLUTION.md) |
