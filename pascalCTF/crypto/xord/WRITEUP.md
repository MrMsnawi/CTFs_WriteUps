# XOR Crypto Challenge Writeup

## Challenge Overview
We're given two files:
- `xord.py` - The encryption script
- `output.txt` - The encrypted flag in hexadecimal format

## Vulnerability Analysis

Looking at the encryption code:

```python
random.seed(1337)
for i in range(len(flag)):
    random_key = random.randint(0, 255)
    encripted_flag += xor(ord(flag[i]), random_key)
```

The critical vulnerability is **the hardcoded random seed (1337)**. This means:
- The "random" numbers are actually **deterministic**
- Anyone who knows the seed can reproduce the exact same sequence
- This completely defeats the purpose of using random keys for XOR encryption

## XOR Properties

XOR encryption has a useful property:
```
If: C = P ⊕ K (ciphertext = plaintext XOR key)
Then: P = C ⊕ K (plaintext = ciphertext XOR key)
```

Since XOR is reversible with the same key, we can decrypt by XORing the ciphertext with the same random values.

## Solution

1. **Initialize the same seed**: `random.seed(1337)`
2. **Generate the same random sequence**: Use the same `random.randint(0, 255)` calls
3. **XOR the encrypted bytes**: Apply XOR with each random key to reverse the encryption

```python
import random

# Read encrypted flag
with open('output.txt', 'r') as f:
    encrypted_hex = f.read().strip()

encrypted_flag = bytes.fromhex(encrypted_hex)

# Use the same seed as the encryption
random.seed(1337)

# Decrypt by reproducing the same random sequence
decrypted_flag = ''
for i in range(len(encrypted_flag)):
    random_key = random.randint(0, 255)
    decrypted_char = encrypted_flag[i] ^ random_key
    decrypted_flag += chr(decrypted_char)

print(decrypted_flag)
```

## Flag
```
pascalCTF{1ts_4lw4ys_4b0ut_x0r1ng_4nd_s33d1ng}
```

## Key Takeaways
- Never use a hardcoded seed for cryptographic purposes
- Pseudo-random number generators (PRNGs) with known seeds are completely predictable
- For real encryption, use cryptographically secure random number generators (CSRNG)
- The flag itself hints at the vulnerability: "it's always about XORing and seeding"
