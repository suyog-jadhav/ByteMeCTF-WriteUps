# Infinity Vault V3 — The Broken Cycle (Cryptography, Hard)

**Author:** Vedant Deore  
**Category:** Crypto  
**Difficulty:** Hard  
**Flag format:** `OWASP{...}`

## Challenge Description

> A damaged vault has been recovered from the Infinity archive. Its observations contain live traces mixed with old archive noise. Reconstruct the current cycle, verify the final state, and follow the trail through the vault. Do not trust a flag-shaped string merely because it decrypts.

## Summary

The live observations must be separated from the archival entries and transformed back into 32-bit states. Those states follow a Linear Congruential Generator (LCG). After verifying the final state, the solver derives a first key, opens the first vault records, rejects two decoy flags, and follows a `NEXT` value to derive the second key and decrypt the real record.

## Flag

```text
OWASP{the_stones_never_lie_twice}
```

---

## Step 1 — Inspect the files and identify the live cycle

The participant files are:

- `README.txt`
- `observations.txt`
- `fragments.txt`
- `vault.bin`
- `seal.txt`

Read `fragments.txt` first. It supplies the initial state, recurrence constants, fixed mask, rotation schedule, number of live traces, and phrases used later in key derivation.

The initial state is:

```text
A17C3E59
```

The entries beginning with `W` belong to the current recorder. The `OLD` entries are archival noise. Use `W00` through `W13` to reconstruct the fourteen-state sequence.

## Step 2 — Reverse the trace transformation

Each live state was transformed before it was written to `observations.txt`:

```text
state
  -> XOR with 0xD1CEB00C
  -> rotate left by (i mod 11) + 3
  -> reverse the four bytes
  -> stored trace
```

Undo the operations in reverse order for each trace index `i`:

1. Reverse the four bytes.
2. Rotate right by `(i mod 11) + 3`.
3. XOR with `0xD1CEB00C`.

Keep each value within 32 bits. Applying the operations in the wrong order will not recover the original states.

## Step 3 — Confirm the recurrence

The recovered values follow the recurrence:

```text
S[n+1] = (1103515245 * S[n] + 12345) mod 2^32
```

The sequence starts at `0xA17C3E59`. Checking consecutive values against the recurrence confirms that the correct observations have been selected and decoded.

The final live state is:

```text
B8812482
```

This value is a witness used for verification; it is not itself the encryption key.

## Step 4 — Verify the final state with `seal.txt`

Calculate SHA-256 over the uppercase, eight-character hexadecimal representation of the final state. Take the first 16 hexadecimal characters and uppercase them.

The expected seal value is:

```text
7EC15BF9D1F285EE
```

A match confirms the state reconstruction.

## Step 5 — Derive the first key

The fragments provide the place `VORMIR` and the phrase `THE_LAST_STONE_REMEMBERS`.

Use the final state's uppercase ASCII hexadecimal representation between those values:

```text
SHA256(
    b"VORMIR" + final_state_ascii + b"THE_LAST_STONE_REMEMBERS"
)[:16]
```

The resulting first key is:

```text
57364b5dc6c0a579b81f578f7ba938c2
```

This key opens the first two records in `vault.bin`. The records use separate domains (`R0` and `R1`) as part of their record-specific decryption.

## Step 6 — Recognize and reject the decoys

The first decrypted record contains a `NEXT` value:

```text
NEXT=7F4A19C2
```

The first two records also reveal these decoy flags:

```text
OWASP{the_last_state_is_the_key}
OWASP{infinity_is_the_answer}
```

Neither is the final answer. The `NEXT` value is the important clue that the vault has another lock.

## Step 7 — Derive the second key

Combine the first key, the recovered `NEXT` value, and the domain phrase `SECOND_ECHO` exactly as follows:

```text
SHA256(key1 + b"|" + b"7F4A19C2" + b"|SECOND_ECHO")[:16]
```

The resulting second key is:

```text
9c063717688e2dcd71459ab6da45666d
```

The second-link seal can be checked by calculating:

```text
SHA256(key1 + b"|" + b"7F4A19C2")
```

Its first 16 uppercase hexadecimal characters are:

```text
1B14A475608CE279
```

## Step 8 — Decrypt the final record

Use the second key on record `R2` in `vault.bin`. The final record reveals:

```text
OWASP{the_stones_never_lie_twice}
```

This is the real flag. The two earlier flag-shaped strings are intentional decoys.

---

## Solution Summary

| Field | Value |
|---|---|
| Initial state | `A17C3E59` |
| LCG multiplier | `1103515245` |
| LCG increment | `12345` |
| Fixed mask | `D1CEB00C` |
| Rotation schedule | `(i mod 11) + 3` |
| Number of live states | 14 |
| Final live state | `B8812482` |
| First key | `57364b5dc6c0a579b81f578f7ba938c2` |
| `NEXT` value | `7F4A19C2` |
| Second key | `9c063717688e2dcd71459ab6da45666d` |
| Real flag | `OWASP{the_stones_never_lie_twice}` |

## Root Cause / Cryptographic Method Explanation

1. **Archive-noise separation** — The challenge includes six old entries alongside fourteen live traces. Only the `W` series belongs to the current cycle.
2. **Reversible trace transformation** — Each 32-bit state is masked with XOR, rotated according to its index, and byte-reversed. The inverse operations must be applied in reverse order.
3. **LCG state reconstruction** — The recovered values follow a Linear Congruential Generator recurrence modulo \(2^{32}\). The recurrence provides a consistency check.
4. **Independent state verification** — `seal.txt` validates the final state separately from the vault decryption.
5. **Chained key derivation** — The first key uses the final state and the two phrases. The second key depends on the first key and the `NEXT` value.
6. **Decoy flags** — Two flag-shaped strings appear in the first layer to catch solvers who stop too early. The real flag is in record `R2`.

## Tools Used

- **Text editor / `cat`** — Read the fragments, observations, and seal.
- **Python** — Reverse the trace transformations, verify the LCG, calculate SHA-256 keys, and decrypt records.
- **`xxd` / hex viewer** — Inspect the binary vault.
- **CyberChef** — Optional for testing byte-level transformations offline.

## Timeline

| Step | Action | Result |
|---|---|---|
| 1 | Read `fragments.txt` | Recover seed, constants, mask, rotation clues, and phrases |
| 2 | Select `W00`–`W13` | Isolate the fourteen live traces |
| 3 | Reverse byte order, rotation, and XOR | Recover the 32-bit states |
| 4 | Test consecutive states against the LCG | Confirm the sequence |
| 5 | Check the final-state seal | Validate `B8812482` |
| 6 | Derive the first key and decrypt `R0`/`R1` | Find two decoys and `NEXT=7F4A19C2` |
| 7 | Derive the second key and decrypt `R2` | Recover the real flag |
