#!/usr/bin/env python3

bs = bytes.fromhex("bffb a4ab f8a5 fb97 bcf8 97ab bbfb 97fd f1f0 a9e9".replace(" ",""))
flag = ''.join(f"{(b^0xc8):02x}" for b in bs)
print(flag)
