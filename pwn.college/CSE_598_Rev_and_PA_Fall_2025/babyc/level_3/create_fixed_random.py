#!/usr/bin/env python3

data = b'random' + b'\x00' * (31-6)
open("/tmp/fixed_random", "wb").write(data)
print("/tmp/fixed_random created " + str(len(data)) + " bytes\n")
