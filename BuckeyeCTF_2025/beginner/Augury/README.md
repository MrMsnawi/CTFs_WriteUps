# Augury — exploit notes

This repository contains a solution script for the "Augury" crypto challenge.

Vulnerability summary
- The service encrypts files by XORing 4-byte blocks with a 32-bit keystream.
- The first 32-bit keystream value is SHAKE-128(password).digest(4) (unknown for the flag).
- Subsequent keystream values are produced by a linear congruential generator (LCG):

    s_{n+1} = (a * s_n + c) mod 2**32

  with a=3404970675 and c=3553295105.

Attack idea
- If you know the first 4 plaintext bytes of a file, you can recover the initial 32-bit seed by XORing those plaintext bytes with the first 4 ciphertext bytes.
- Many CTF flags have predictable prefixes (e.g., `flag{`, `CTF{`). Try several common 4-byte prefixes to immediately recover the seed.
- Once the seed is known, run the LCG to recover all subsequent keystream blocks and decrypt the file.

Files
- `exploit.py` — pwntools script that connects to the remote service, lists files, fetches ciphertext hex for candidate files and tries to decrypt them using the above technique.

Usage
1. Install pwntools:

```bash
pip install pwntools
```

2. Run the exploit:

```bash
python3 exploit.py
```

Notes
- If the remote service uses a non-standard flag format, expand the prefix list or let the script brute-force printable 4-byte prefixes (this can be slow but is implemented as a fallback).
- If network access is blocked, you can adapt the decryption logic in `exploit.py` to test locally by providing a ciphertext hex string.
