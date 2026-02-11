#!/usr/bin/env python3
"""
FlagYard - SlowScript (Reversing)

The challenge gives us a Python script that is obfuscated with 50 nested layers
of: reverse -> base64 decode -> zlib decompress -> exec

After peeling all layers, the inner code is:

    enc_flag = [71,209,120,114,232,150,255,119,82,46,31,23,35,43,28,144,
                246,78,184,177,20,156,237,54,21,188,91,84,226,104,223,85,
                182,11,169,164,6,9,52]
    tmp = 31337
    for i in range(len(enc_flag)):
        fn = tmp ** i
        sm = 0
        for j in range(fn + 1):   # <-- intentionally slow
            sm += j
        print(chr((sm % 256) ^ enc_flag[i]), end='')

The decryption XORs each byte with (sum(0..31337^i)) % 256.
The naive summation loop makes this impossibly slow for i > 1 since 31337^i
grows astronomically. Replace it with the closed-form triangular number
formula: sum(0..n) = n * (n + 1) // 2
"""

import zlib, base64, re

# --- Step 1: Peel all 50 obfuscation layers ---

decode = lambda blob: zlib.decompress(base64.b64decode(blob[::-1]))

with open("challenge.py") as f:
    code = f.read()

layers = 0
while True:
    match = re.search(r"\(_\)\(b'([^']+)'\)", code)
    if not match:
        break
    code = decode(match.group(1).encode()).decode()
    layers += 1

print(f"[*] Peeled {layers} obfuscation layers")

# --- Step 2: Extract the encrypted flag array ---

match = re.search(r"enc_flag=\[([^\]]+)\]", code)
enc_flag = list(map(int, match.group(1).split(",")))

match = re.search(r"tmp=(\d+)", code)
tmp = int(match.group(1))

# --- Step 3: Decrypt using closed-form triangular number ---

flag = ""
for i in range(len(enc_flag)):
    fn = tmp ** i
    sm = fn * (fn + 1) // 2  # O(1) instead of O(31337^i)
    flag += chr((sm % 256) ^ enc_flag[i])

print(f"[+] Flag: {flag}")
