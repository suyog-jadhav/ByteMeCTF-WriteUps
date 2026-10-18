# Soul Stone — The Forgotten Echo (Cryptography, Hard+)

**Author:** Vedant Deore 
**Category:** Crypto  
**Difficulty:** Hard  
**Flag format:** `OWASP{...}`

## Challenge Description

> The Soul Stone was never supposed to keep a copy of the truth. What survived the last transfer is a collection of fragments, an archival seal, and two pieces of ciphertext. Some material is useful; some was deliberately left behind to look useful. The challenge is completely offline, and finding one recognizable encoding does not mean the plaintext has been reached.

## Summary

The fragments reveal a phrase and a location. These are combined to derive a key that opens an intermediate binary. That intermediate message contains two decoy flags and a clue for a second encrypted layer. Reversing the second layer's grouped hexadecimal and applying a derived XOR key reveals the actual flag.

## Flag

```text
OWASP{the_soul_stone_remembers_twice}
```

---

## Step 1 — Read the fragments

Start with `fragments.txt`. The clue says:

> “The first sacrifice opens what the last one cannot.”

This suggests examining the beginning of each line. Taking the first character of every line produces:

```text
SACRIFICEOPENSTHEECHO
```

Add natural word spacing:

```text
SACRIFICE OPENS THE ECHO
```

This is the first piece of key material.

## Step 2 — Recover the location

The first six lines contain another extraction. Take the final character of the last word on each of those six lines:

```text
V O R M I R
```

This spells:

```text
VORMIR
```

The recovered phrase and location are used together, rather than treating either as a complete key on its own.

## Step 3 — Derive the first key

Normalize the phrase exactly as `SACRIFICE OPENS THE ECHO`, then append a pipe and the location:

```text
SACRIFICE OPENS THE ECHO|VORMIR
```

Calculate SHA-256 over that exact text. The digest begins:

```text
578c26bdb6a03e93b57e4dd2628ff526...
```

Use the first 16 bytes of the digest as the key for `echo.bin`:

```text
578c26bdb6a03e93b57e4dd2628ff526
```

The exact spacing and separator matter.

## Step 4 — Reverse the `echo.bin` transformations

`echo.bin` has more than one transformation. Its encryption sequence is:

```text
plaintext
  -> repeating-key XOR
  -> rotate each byte left by (position mod 7) + 1
  -> reverse the entire byte array
  -> echo.bin
```

To decrypt, undo these operations in reverse order:

1. Reverse the byte array.
2. Rotate each byte right by `(position mod 7) + 1`.
3. XOR with the repeating 16-byte key.

The recovered message includes:

```text
The echo is a mirror, not a destination.
OWASP{the_soul_stone_is_the_key}
OWASP{first_echo_is_always_true}
The final voice is still waiting. Reverse the groups before listening.
```

The two flag-shaped strings are decoys. The instruction at the end points to a separate encrypted layer.

## Step 5 — Decode the final vault

Open `vault.txt`. The ciphertext is represented as hexadecimal data split into groups of eight characters. Each group has been reversed.

Reverse every 8-character group first. Convert the corrected hexadecimal string into bytes; the result is still XOR-encrypted.

The second key is derived from the first key:

```text
SHA256(first_key_bytes + b"SECOND_ECHO")[:12]
```

This gives the 12-byte repeating key:

```text
755e34baa90ec9d8f62aa322
```

XOR the corrected ciphertext bytes with this key repeatedly to recover the final plaintext.

## Step 6 — Confirm the flag

The final plaintext is:

```text
OWASP{the_soul_stone_remembers_twice}
```

Do not submit either of the flag-shaped strings found in the intermediate echo. They are intentional decoys.

---

## Solution Summary

| Field | Value |
|---|---|
| Initial phrase | `SACRIFICE OPENS THE ECHO` |
| Location salt | `VORMIR` |
| First key derivation | `SHA256("SACRIFICE OPENS THE ECHO|VORMIR")[:16 bytes]` |
| `echo.bin` layers | Repeating XOR, position-based byte rotation, whole-array reversal |
| Second key derivation | `SHA256(first_key_bytes + b"SECOND_ECHO")[:12 bytes]` |
| Final `vault.txt` layers | Reverse each 8-character hex group, hex-decode, repeating XOR |
| Real flag | `OWASP{the_soul_stone_remembers_twice}` |

## Root Cause / Cryptographic Method Explanation

1. **Extraction from natural-language fragments** — The first character of every line encodes the phrase. The final characters from the first six lines encode the location.
2. **Key derivation** — SHA-256 combines the phrase and location into key material. The digest is truncated to the required key length.
3. **Reversible byte transformations** — The echo is transformed with repeating XOR, position-dependent rotation, and byte-array reversal. Decryption must undo these in reverse order.
4. **Decoy handling** — Two valid-looking flags are deliberately placed in the intermediate plaintext. The instruction to reverse groups signals that another layer remains.
5. **Second-stage decryption** — The final vault uses a key derived from the first key. Its ciphertext must first be restored by reversing each 8-character hexadecimal group.

## Tools Used

- **Text editor / `cat`** — Inspect the fragment clues and ciphertext files.
- **Python** — Extract characters, calculate SHA-256, reverse byte transformations, and apply repeating XOR.
- **`xxd`** — Inspect binary and hexadecimal data.
- **CyberChef** — Optional way to test the transformations offline.

## Timeline

| Step | Action | Result |
|---|---|---|
| 1 | Read the first character of each fragment line | `SACRIFICE OPENS THE ECHO` |
| 2 | Read the final characters of the first six lines | `VORMIR` |
| 3 | Hash phrase and location | First 16-byte key |
| 4 | Reverse the transformations on `echo.bin` | Intermediate message and two decoys |
| 5 | Reverse each 8-character group in `vault.txt` | Corrected hexadecimal ciphertext |
| 6 | Derive the second key and apply repeating XOR | Real flag recovered |
