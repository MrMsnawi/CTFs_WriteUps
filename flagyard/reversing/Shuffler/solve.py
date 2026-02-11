#!/usr/bin/env python3
import random
import hashlib

with open('flag.enc', 'r') as enc:
    encFlag = enc.read()

while True:
    flag = ''
    simp = [encFlag[i:i+8] for i in range(0, 40, 8)]
    random.shuffle(simp)

    flat = ''.join(simp)
    
    for i in range(40):
        flag += chr(ord(flat[i]) ^ (i << 3))
    
    if hashlib.md5(flag[:39].encode()).hexdigest() == "ac9dc5b77c199d4737f5010da0fcdd24":
        print("Found the flag!")
        print(flag[:39])
        break

