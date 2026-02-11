#!/usr/bin/env python3

# Open and read the filter file
with open('filter', 'r') as f:
    content = f.read()

hex_bytes = []

# Extract the last hex value from each line (the comparison value)
for line in content.strip().split('\n'):
    if ',0x' in line:
        # Find the hex value after ",0x"
        parts = line.split(',0x')
        if len(parts) > 1:
            # Get the hex value (first 2 characters after 0x)
            hex_val = parts[-1].strip()[:2]
            hex_bytes.append(hex_val)

# Reverse the order of hex bytes
hex_bytes.reverse()

# Convert all hex values to a string
hex_string = ''.join(hex_bytes)
result = bytes.fromhex(hex_string).decode('utf-8', errors='ignore')
print(result)
