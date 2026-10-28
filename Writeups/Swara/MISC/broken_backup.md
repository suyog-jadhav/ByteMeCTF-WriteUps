# Broken Backup (Misc / Crypto, Easy-Medium)

**Author:** Swara Shirke  
**Category:** Misc / Cryptography  
**Difficulty:** Easy–Medium  
**Flag Format:** `OWASP{...}`

---

## Challenge Description

> A suspicious backup has been recovered from a compromised system. The backup contains multiple files, including logs, configuration data, and a binary backup file. At first glance, everything appears normal, but something in the configuration may reveal how the backup data was protected.
>
> **Task:** Investigate the provided files, identify the weakness, and recover the hidden flag.

**Challenge Files:**
- `backup.log` — Contains information about the backup process.
- `config.ini` — Contains configuration values.
- `backup.dat` — Contains the protected/hidden data.

---

## Summary

*Broken Backup* is a file-based challenge exploring data obfuscation via XOR. An analysis of `config.ini` reveals an anomalous configuration value `version=66`. Converting the decimal value $66_{10}$ to hexadecimal gives `0x42`. Using `0x42` as a single-byte XOR key against `backup.dat` reverses the obfuscation and recovers the flag.

---

## Flag

```text
OWASP{xor_is_not_encryption}
```

---

## Intended Solve Path

```text
Inspect files ➔ Examine config.ini ➔ Suspicious value: 66 ➔ Decimal 66 to Hex 0x42 ➔ Test 0x42 as XOR key ➔ Decrypt backup.dat ➔ Flag
```

---

## Step-by-Step Solution

### Step 1 — Inspect the Configuration
Examining the challenge files reveals `config.ini`. Inside the configuration, one line stands out:

```ini
[system]
env=production
version=66
status=archived
```

The integer `66` is unusual for a semantic version number and warrants closer inspection.

### Step 2 — Representation Analysis
Converting decimal `66` to different number representations:
- **Decimal:** `66`
- **Hexadecimal:** `0x42` (ASCII character `'B'`)
- **Binary:** `01000010`

### Step 3 — XOR Reversibility
XOR is a symmetric operation:
$$\text{Ciphertext} \oplus \text{Key} = \text{Plaintext}$$

Testing `0x42` as a candidate single-byte XOR key on `backup.dat`.

### Step 4 — XOR Decryption Script

```python
with open("backup.dat", "rb") as f:
    data = f.read()

decrypted = bytes(byte ^ 0x42 for byte in data)
print(decrypted.decode())
```

**Output:**
```text
OWASP{xor_is_not_encryption}
```

---

## Key Takeaways
1. Always inspect configuration files for hidden constants and seeds.
2. Consider alternative radix representations (decimal ↔ hexadecimal).
3. XOR with a static single-byte key provides obfuscation, not cryptographically secure encryption.
