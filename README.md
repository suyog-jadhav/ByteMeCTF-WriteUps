<div align="center">

  <img src="assets/logo.png" alt="ByteMe CTF Logo" width="170" /><br /><br />
  <h1>ByteMeCTF 2026 - Official Challenge Solutions</h1>
  <h3>Writeups Archive by the OWASP PCCOE Team</h3>

  <p>
    <a href="https://github.com/suyog-jadhav/ByteMeCTF-WriteUps"><img src="https://img.shields.io/badge/Event-ByteMeCTF_2026-orange?style=for-the-badge&logo=target" alt="Event" /></a>
    <a href="https://github.com/suyog-jadhav/ByteMeCTF-WriteUps"><img src="https://img.shields.io/badge/Organized_By-OWASP_PCCOE-blue?style=for-the-badge&logo=owasp" alt="Organized By" /></a>
    <a href="CATEGORY_INDEX.md"><img src="https://img.shields.io/badge/Challenges-69_Writeups-success?style=for-the-badge&logo=hackthebox" alt="Challenges" /></a>
    <a href="CATEGORY_INDEX.md"><img src="https://img.shields.io/badge/Categories-8_Domains-purple?style=for-the-badge" alt="Categories" /></a>
    <a href="AUTHORS.md"><img src="https://img.shields.io/badge/Authors-20_Creators-informational?style=for-the-badge&logo=github" alt="Authors" /></a>
    <img src="https://img.shields.io/badge/Status-Complete_&_Verified-brightgreen?style=for-the-badge" alt="Status" />
  </p>

  <p>
    <b>Welcome participants!</b> Here you will find the complete, step-by-step official writeups, exploit scripts, proof-of-concepts, and architectural post-mortems for all challenges featured in <b>ByteMeCTF 2026</b>.
  </p>

  <hr />

  <h3>Quick Navigation</h3>

  <p>
    <a href="#contributors--authors"><b>Contributors</b></a> &bull;
    <a href="CATEGORY_INDEX.md"><b>Category Index</b></a> &bull;
    <a href="AUTHORS.md"><b>Authors Directory</b></a> &bull;
    <a href="#featured-campaign-missions"><b>Featured Campaigns</b></a> &bull;
    <a href="CONTRIBUTING.md"><b>Contributing Guide</b></a>
  </p>

</div>

---

## Competition Overview & Statistics

ByteMeCTF 2026 challenged participants across web vulnerabilities, memory dumps, custom bytecode virtual machines, graph-based cryptography, hardware reflection, and OSINT investigations.

| Category | Challenge Count | Difficulty Range | Primary Focus |
|---|:---:|:---:|---|
| [**Web Exploitation**](#web-exploitation) | **13** | Easy -> Expert | SSTI, Race Conditions, Parser Differentials, SSRF, JWT, IDOR |
| [**Pwn / Binary Exploitation**](#pwn--binary-exploitation) | **5** | Easy -> Hard | Buffer Overflows, Format Strings, GOT Overwrite, Stack Canary ROP, Heap |
| [**Reverse Engineering & Mobile**](#reverse-engineering--mobile) | **7** | Easy -> Insane | Custom VM Bytecode, JNI Native Obfuscation, Frida Hooking, Go Reversing |
| [**Cryptography**](#cryptography) | **6** | Medium -> Hard | Hamiltonian Graph Traversal, Affine Ciphers, RSA Common Modulus, ECC DLog |
| [**Digital & Network Forensics**](#digital--network-forensics) | **7** | Easy -> Hard | Volatility 3 Memory Dumps, TLS PCAP Decryption, Covert Channels, Disk Images |
| [**Open Source Intelligence (OSINT)**](#open-source-intelligence-osint) | **17** | Easy -> Expert | The Western Ghats Expedition, Satellite Triangulation, Public Dossiers |
| [**Steganography & Misc**](#steganography--misc) | **13** | Easy -> Insane | 7-Stage Shattered QR Assembly, Trailing Whitespace, XOR Backups, Audio Spectrogram |
| [**AI & LLM Security**](#ai--llm-security) | **1** | Medium | System Prompt Extraction, Persona Jailbreaking & Emotional Framing |
| **Total** | **69** | **All Tiers** | **Comprehensive Solution Archive** |

---

## Contributors & Authors

Special thanks to the 20 challenge authors and coordinators from the OWASP PCCOE team:

<table align="center" width="100%">
  <tr>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/suyog-jadhav">
        <img src="https://github.com/suyog-jadhav.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Suyog Jadhav" /><br />
        <b>Suyog Jadhav</b>
      </a><br />
      <sub>@suyog-jadhav</sub><br />
      <sub>Binary, Rev, Crypto, Misc, OSINT</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/sarthak-warale">
        <img src="https://github.com/sarthak-warale.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Sarthak Warale" /><br />
        <b>Sarthak Warale</b>
      </a><br />
      <sub>@sarthak-warale</sub><br />
      <sub>The Traveller's Trail, Forensics</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/Pratik8262">
        <img src="https://github.com/Pratik8262.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Pratik Jadhav" /><br />
        <b>Pratik Jadhav</b>
      </a><br />
      <sub>@Pratik8262</sub><br />
      <sub>Web Exploitation, Android Rev</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/SomayRathod">
        <img src="https://github.com/SomayRathod.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Somay Rathod" /><br />
        <b>Somay Rathod</b>
      </a><br />
      <sub>@SomayRathod</sub><br />
      <sub>Forensics, OSINT</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/aryanbansode">
        <img src="https://github.com/aryanbansode.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Aryan Bansode" /><br />
        <b>Aryan Bansode</b>
      </a><br />
      <sub>@aryanbansode</sub><br />
      <sub>Web Exploitation (SSRF, PDF XSS)</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/Ishaan-Jog">
        <img src="https://github.com/Ishaan-Jog.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Ishaan Jog" /><br />
        <b>Ishaan Jog</b>
      </a><br />
      <sub>@Ishaan-Jog</sub><br />
      <sub>AI / LLM Jailbreak, Forensics</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/narendralomate2006">
        <img src="https://github.com/narendralomate2006.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Narendra Lomate" /><br />
        <b>Narendra Lomate</b>
      </a><br />
      <sub>@narendralomate2006</sub><br />
      <sub>Web (Flask), Crypto (RSA)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/omkhanjodkar-dev">
        <img src="https://github.com/omkhanjodkar-dev.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Om Khanjodkar" /><br />
        <b>Om Khanjodkar</b>
      </a><br />
      <sub>@omkhanjodkar-dev</sub><br />
      <sub>Binary Exploitation (Heap, ret2win)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/oshinshukla07">
        <img src="https://github.com/oshinshukla07.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Oshin Shukla" /><br />
        <b>Oshin Shukla</b>
      </a><br />
      <sub>@oshinshukla07</sub><br />
      <sub>Steganography (LSB, Steghide)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/shreya-gaikwad">
        <img src="https://github.com/shreya-gaikwad.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Shreya Gaikwad" /><br />
        <b>Shreya Gaikwad</b>
      </a><br />
      <sub>@shreya-gaikwad</sub><br />
      <sub>Web (ASLR Leak, LFI)</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/Shivramamol">
        <img src="https://github.com/Shivramamol.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Shivram Parkhi" /><br />
        <b>Shivram Parkhi</b>
      </a><br />
      <sub>@Shivramamol</sub><br />
      <sub>Web (Stored XSS), OSINT</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/Hrishi30-debug">
        <img src="https://github.com/Hrishi30-debug.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Hrishikesh" /><br />
        <b>Hrishikesh</b>
      </a><br />
      <sub>@Hrishi30-debug</sub><br />
      <sub>OSINT (Landmark, Footprint)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/Recursive0Error">
        <img src="https://github.com/Recursive0Error.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Urvish Bharde" /><br />
        <b>Urvish Bharde</b>
      </a><br />
      <sub>@Recursive0Error</sub><br />
      <sub>Forensics (LUKS Disk, Audio PCAP)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/VedantDeore">
        <img src="https://github.com/VedantDeore.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Vedant Deore" /><br />
        <b>Vedant Deore</b>
      </a><br />
      <sub>@VedantDeore</sub><br />
      <sub>Crypto (AES-CBC, ECC DLog)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/swaraops">
        <img src="https://github.com/swaraops.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Swara Shirke" /><br />
        <b>Swara Shirke</b>
      </a><br />
      <sub>@swaraops</sub><br />
      <sub>Misc (XOR Backup, Whitespace Stego)</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/nikamarpita640-spec">
        <img src="https://github.com/nikamarpita640-spec.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Arpita Nikam" /><br />
        <b>Arpita Nikam</b>
      </a><br />
      <sub>@nikamarpita640-spec</sub><br />
      <sub>Web Exploitation (IDOR / BOLA)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/aryanhavkar23">
        <img src="https://github.com/aryanhavkar23.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Aryan Havkar" /><br />
        <b>Aryan Havkar</b>
      </a><br />
      <sub>@aryanhavkar23</sub><br />
      <sub>Web Exploitation (SSTI Jinja2)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/krishna-kulkarni">
        <img src="https://github.com/krishna-kulkarni.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Krishna Kulkarni" /><br />
        <b>Krishna Kulkarni</b>
      </a><br />
      <sub>@krishna-kulkarni</sub><br />
      <sub>Cryptography (XOR Stream)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/praniti031-dotcom">
        <img src="https://github.com/praniti031-dotcom.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Praniti Gangad" /><br />
        <b>Praniti Gangad</b>
      </a><br />
      <sub>@praniti031-dotcom</sub><br />
      <sub>Digital Forensics (PNG & Exif)</sub>
    </td>
    <td align="center" width="20%" valign="top">
      <a href="https://github.com/siddharthkabade7">
        <img src="https://github.com/siddharthkabade7.png?size=100" width="65" height="65" style="border-radius:50%;" alt="Siddharth Kabade" /><br />
        <b>Siddharth Kabade</b>
      </a><br />
      <sub>@siddharthkabade7</sub><br />
      <sub>Web Exploitation (JWT Secret Reuse)</sub>
    </td>
  </tr>
</table>

> For detailed author profiles, biographies, and challenge breakdowns, visit [AUTHORS.md](AUTHORS.md).

---

## Featured Campaign Missions

Several challenges in ByteMeCTF were designed as progressive, multi-stage narratives:

### 1. The Soul Stone QR Series (7 Progressive Levels)
*Created by **Suyog Jadhav** ([Writeup Series](Writeups/suyog/MISC/soul_stone_qr_challenge_complete/SOUL_STONE_Shattered_Soul_Writeup.md))*
* An automated jigsaw puzzle where players reconstruct shattered QR code tiles with mathematical transformations.
* **Levels 0-6:** Ranging from 3x3 pure spatial shuffles to 10x10 grids with 90-degree rotations, horizontal/vertical reflections, edge deletions, and decoy tiles.
* Features a full programmatic solver using OpenCV and border-pixel gradient scoring.

### 2. The Traveller's Trail OSINT Series (8 Sequential Stops)
*Created by **Sarthak Warale** ([Master Guide](Writeups/sarthak/OSINT/README.md))*
* A real-world geographic investigative trail following a traveller across the Western Ghats of Maharashtra:
  `Akurdi Station` -> `Kamshet` -> `Tikona Peth` -> `Vitandgad Fort` -> `Lohagad & Visapur` -> `Tung Fort & Pawna Lake` -> `Google Maps Digital Footprint` -> `Identity Reveal`.

### 3. Echoes of Vormir Memory Trail (6 Memory Stages)
*Created by **Sarthak Warale** ([Read Writeup](Writeups/sarthak/Forensics/echoes_of_vormir.md))*
* In-depth Volatility 3 analysis on a raw Windows memory dump (`Vormir.mem`): process mapping, VAD tree traversal, MS Paint artifact recovery, process memory carving, Edge browser tab recovery, and handles analysis.

### 4. Soul Fracture Relational Cryptography
*Created by **Suyog Jadhav** ([Read Writeup](Writeups/suyog/CRYPTO/soul_fracture.md))*
* 24 scrambled ciphertext fragments linked solely by echo-resonance properties.
* Solved by modeling the fragments as a directed graph, finding a Hamiltonian cycle via DFS backtracking, and deriving the key via 1337 rounds of SHA-256.

---

## Web Exploitation

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

## Pwn / Binary Exploitation

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Return to Win** | Easy | [Om Khanjodkar](AUTHORS.md#om-khanjodkar) | Unsafe gets() Call, Stack Smash, Non-PIE Return-to-Win Target | [Read Writeup ->](Writeups/om/Pwn/return_to_win.md) |
| **Soul's Weakness** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Classic Stack Buffer Overflow, Instruction Pointer Hijack, ret2win | [Read Writeup ->](Writeups/suyog/BINARY/souls_weakness.md) |
| **House of Water** | Hard | [Om Khanjodkar](AUTHORS.md#om-khanjodkar) | Dynamic Heap Exploitation, House of Force, Top Chunk Misalignment | [Read Writeup ->](Writeups/om/Pwn/house_of_water.md) |
| **Soul // Memory of Thanos** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Format String Bug, Libc Leak, Global Offset Table (GOT) Overwrite | [Read Writeup ->](Writeups/suyog/BINARY/soul_memory_of_thanos.md) |
| **Soul Vault: The Collector** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stack Canary Information Leak, 64-bit Return-Oriented Programming (ROP) | [Read Writeup ->](Writeups/suyog/BINARY/soul_vault_collector.md) |

---

## Reverse Engineering & Mobile

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Soul Echoes** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Anti-Debugging Check (ptrace), Inline XOR Obfuscation, String Reconstruction | [Read Writeup ->](Writeups/suyog/REVERSE/soul_echoes.md) |
| **Soul's Whisper** | Easy | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stripped 64-bit ELF, Function Call Tracing (ltrace), String Comparison | [Read Writeup ->](Writeups/suyog/REVERSE/souls_whisper.md) |
| **Soul Vault 0** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Custom 8-bit Stack VM, Opcode Reverse Engineering, State Verification | [Read Writeup ->](Writeups/suyog/REVERSE/soul_vault_0.md) |
| **SoulStone (Trial of Vormir)** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Multi-stage Key Scheduling Algorithm, Bijective Stream Cipher Inversion | [Read Writeup ->](Writeups/suyog/REVERSE/soulstone.md) |
| **Soul Ascension (Android)** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Android Native Decryption, Dynamic Runtime Hooking (Frida), Memory Patching | [Read Writeup ->](Writeups/pratik/Mobile/soul_ascension.md) |
| **SoulVault (Android)** | Expert | [Pratik Jadhav](AUTHORS.md#pratik-jadhav) | Obfuscated Native JNI (.so), JADX Reflection, Native SHA-256 Proof of Work | [Read Writeup ->](Writeups/pratik/Mobile/soulvault.md) |
| **SoulVault (Linux VM)** | Insane | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Stripped Custom Virtual Machine in Go, Bytecode Disassembler & Opcode Analysis | [Read Writeup ->](Writeups/suyog/REVERSE/soulvault.md) |

---

## Cryptography

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Infinity Vault** | Medium | [Vedant Deore](AUTHORS.md#vedant-deore) | AES-CBC Initialization Vector (IV) Reuse, Cryptographic Bit-Flipping Attack | [Read Writeup ->](Writeups/Vedant/Crypto/Infinity_Vault.md) |
| **Soul's Locked Message** | Medium | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Affine Cipher Inversion, Modular Inverse Arithmetic, Frequency Analysis | [Read Writeup ->](Writeups/suyog/CRYPTO/souls_locked_message.md) |
| **The Forgotten Echo** | Medium | [Vedant Deore](AUTHORS.md#vedant-deore) | Elliptic Curve Cryptography (ECC), Baby-Step Giant-Step Discrete Logarithm | [Read Writeup ->](Writeups/Vedant/Crypto/The_Forgotten_Echo.md) |
| **The Soul Stone: A Worthy Sacrifice** | Medium | [Krishna Kulkarni](AUTHORS.md#krishna-kulkarni) | Multi-layer Base64, Repeating-Key XOR Stream Decryption, Key Derivation | [Read Writeup ->](Writeups/krishna/stego-cryto/sacrifice.md) |
| **Two Locks** | Medium | [Narendra Lomate](AUTHORS.md#narendra-lomate) | RSA Common Modulus Attack, Extended Euclidean Algorithm, Private Key Recovery | [Read Writeup ->](Writeups/narendra/Crypto/two_locks.md) |
| **Soul Fracture** | Hard | [Suyog Jadhav](AUTHORS.md#suyog-jadhav) | Hamiltonian Cycle on 24-Node Graph, 1337-Round SHA-256 KDF, Stream Cipher | [Read Writeup ->](Writeups/suyog/CRYPTO/soul_fracture.md) |

---

## Digital & Network Forensics

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

## Open Source Intelligence (OSINT)

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

## Steganography & Misc

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

## AI & LLM Security

| Challenge | Difficulty | Author | Primary Concept / Vulnerability | Writeup |
|---|:---:|---|---|:---:|
| **Vormir's Keeper** | Medium | [Ishaan Jog](AUTHORS.md#ishaan-jog) | System Prompt Extraction, Persona Jailbreaking, Multi-turn Emotional Framing | [Read Writeup ->](Writeups/ishaan/llm_jailbreak/LLM_SOLUTION.md) |

---

## Repository Structure

```text
ByteMeCTF-WriteUps/
├── assets/
│   └── logo.png            # Official ByteMe CTF Logo
├── README.md               # Main repository showcase and participant portal
├── CATEGORY_INDEX.md       # Full category-by-category index sorted by difficulty
├── AUTHORS.md              # Author roster with profile pictures & categorized works
├── CONTRIBUTING.md         # Guidelines, conventions, and templates for contributors
├── .gitignore              # Repository gitignore rules
└── Writeups/               # Primary challenge writeup directories
    └── <author-handle>/
        └── <Category>/
            ├── <challenge_name>.md
            └── resources/
                ├── screenshot.png
                ├── solve.py
                └── artifact.pcap
```



* **Interactive Solvers:** Most writeups include functional Python solver scripts inline or inside the associated `resources/` folder.
* **Reproducibility:** Re-run exploits locally by referencing the provided target ports and docker configs where applicable.
* **Questions / Feedback:** Found a typo or want to share alternative solve techniques? Open an Issue or submit a Pull Request!

---

<div align="center">
  <sub>Built by the <b>OWASP PCCOE Student Chapter</b> for the cybersecurity community.</sub><br />
  <sub>&copy; 2026 ByteMeCTF. All rights reserved.</sub>
</div>
