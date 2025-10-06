#!/usr/bin/env python3

from pwn import *

def print_lines(p):
    while True:
        out = None
        try:
            out = p.recvline(timeout=2)
            if out != None:
                print(out.decode())
            else:
                return
        except EOFError:
            break

context(arch="amd64", os="linux", log_level="info")

program = "/challenge/pwntools-tutorials-level3.0"

payload = [b"hello ", b"world,", b"nop", b"magic ", b"nop", b"notebook"]

p = process(program)

i = 0
while i < 6:
    if i != 2 and i != 4:
        p.sendafter(b"Choice >> \n", b"1\n")
        p.sendafter(b"Input your notebook index:\n", (str(i) + '\n').encode())
        p.sendafter(b"Input your notebook content:\n", payload[i])
        #print(payload[i])
        print(i)
    if i == 1 or i == 5:
        p.sendafter(b"Choice >> \n", b"2\n")
        p.sendafter(b"Input your notebook index:\n", (str(i) + '\n').encode())
        #print("edit")
        print(i)
    if i == 2 or i == 4:
        p.sendafter(b"Choice >> \n", b"1\n")
        p.sendafter(b"Input your notebook index:\n", (str(i) + '\n').encode())
        p.sendafter(b"Input your notebook content:\n", b"nop\n")
        #print("nop")
        print(i)
    i += 1

p.sendafter(b"Choice >> \n", b"5\n")
print_lines(p)
p.interactive()
