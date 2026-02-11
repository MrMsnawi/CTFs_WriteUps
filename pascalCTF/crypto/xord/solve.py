import random

# Read the encrypted flag from output.txt
with open('output.txt', 'r') as f:
    encrypted_hex = f.read().strip()

# Convert hex to bytes
encrypted_flag = bytes.fromhex(encrypted_hex)

# The vulnerability: the random seed is hardcoded to 1337
# We can reproduce the exact same "random" sequence
random.seed(1337)

# Decrypt by XORing with the same random values
decrypted_flag = ''
for i in range(len(encrypted_flag)):
    random_key = random.randint(0, 255)
    decrypted_char = encrypted_flag[i] ^ random_key
    decrypted_flag += chr(decrypted_char)

print("Decrypted flag:", decrypted_flag)
