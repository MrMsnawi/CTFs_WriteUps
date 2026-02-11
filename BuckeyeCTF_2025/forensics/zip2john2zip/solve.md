# zip2john2zip - CTF Writeup

**Challenge Name:** zip2john2zip  
**Category:** Forensics / Crypto  
**Difficulty:** Medium  
**Flag:** `bctf{not_all_hashes_are_hashed_equally}`

---

## Challenge Description

We are given only a hash file (`hash.txt`) containing a pkzip2 hash. The challenge name hints at the solution path: `zip2john2zip` - suggesting we need to go from a hash back to extracting the original data, but **without the original ZIP file**.

## Given Files

**hash.txt:**
```
flag.zip/flag.txt:$pkzip2$1*1*2*0*34*28*64ac0ae2*0*26*0*34*64ac*a388*2c386d49756e1d70ab5f2d8b7ccf1703b28d2775e84d89ccf4bf26d0e735e9a817b0032b5071540889c34b9331b694d6042c30a0*$/pkzip2$:flag.txt:flag.zip::flag.zip
```

## Solution

### Step 1: Crack the Password with John the Ripper

First, we need to crack the password from the pkzip2 hash using John the Ripper:

```bash
# Using John the Ripper Jumbo version
./john/run/john --format=PKZIP hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

Output:
```
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Cracked 1 password hash (is in ./john/run/john.pot), use "--show"
```

View the cracked password:
```bash
./john/run/john --show hash.txt
```

Output:
```
flag.zip/flag.txt:factfinder:flag.txt:flag.zip::flag.zip
1 password hash cracked, 0 left
```

**Password found:** `factfinder`

### Step 2: Understanding the Challenge

At this point, most CTF challenges would require you to have the original `flag.zip` file to extract with the password. However, the challenge name "zip2john2zip" and the fact that no ZIP file is provided suggests something different.

The key insight: **The pkzip2 hash contains the encrypted data itself!**

### Step 3: Parse the pkzip2 Hash Format

The pkzip2 hash format contains several fields separated by asterisks:

```
$pkzip2$*version*cipher*comp_type*?*comp_size*uncomp_size*crc32*?*?*?*?*checkbytes*checkbytes*encrypted_data*$/pkzip2$
```

Breaking down our hash:
- **Field 0:** `1` - Version
- **Field 1:** `1` - Cipher type (traditional PKZIP encryption)
- **Field 2:** `2` - Compression method (2 = stored/no compression)
- **Field 3:** `0` - Unknown
- **Field 4:** `34` (hex) = 52 bytes - Compressed size
- **Field 5:** `28` (hex) = 40 bytes - Uncompressed size  
- **Field 6:** `64ac0ae2` - CRC32 checksum
- **Fields 7-12:** Various checksums and metadata
- **Field 13:** `2c386d49756e1d70ab5f2d8b7ccf1703b28d2775e84d89ccf4bf26d0e735e9a817b0032b5071540889c34b9331b694d6042c30a0` - The encrypted data!

### Step 4: Implement PKZIP Traditional Encryption Decryption

PKZIP Traditional Encryption uses a stream cipher based on three 32-bit keys. Here's the decryption algorithm:

```python
#!/usr/bin/env python3
"""
Manual PKZIP Traditional Encryption decryption
"""

class PKZIPDecrypter:
    def __init__(self, password):
        self.keys = [0x12345678, 0x23456789, 0x34567890]
        for c in password:
            self._update_keys(ord(c))
    
    def _update_keys(self, c):
        self.keys[0] = self._crc32(self.keys[0], c)
        self.keys[1] = (self.keys[1] + (self.keys[0] & 0xFF)) & 0xFFFFFFFF
        self.keys[1] = (self.keys[1] * 134775813 + 1) & 0xFFFFFFFF
        self.keys[2] = self._crc32(self.keys[2], self.keys[1] >> 24)
    
    def _crc32(self, crc, c):
        """Calculate CRC32 using standard polynomial"""
        crc_table = []
        for i in range(256):
            c_val = i
            for j in range(8):
                if c_val & 1:
                    c_val = 0xEDB88320 ^ (c_val >> 1)
                else:
                    c_val = c_val >> 1
            crc_table.append(c_val)
        
        return crc_table[(crc ^ c) & 0xFF] ^ (crc >> 8)
    
    def decrypt(self, c):
        """Decrypt a single byte"""
        temp = self.keys[2] | 2
        c = c ^ (((temp * (temp ^ 1)) >> 8) & 0xFF)
        self._update_keys(c)
        return c

# Read hash and extract encrypted data
with open('hash.txt', 'r') as f:
    hash_line = f.read().strip()

parts = hash_line.split('$pkzip2$')
fields = parts[1].split('*')

encrypted_hex = fields[13]
encrypted_data = bytes.fromhex(encrypted_hex)

print(f"[+] Encrypted data: {len(encrypted_data)} bytes")

# Decrypt with password
password = "factfinder"
decrypter = PKZIPDecrypter(password)

decrypted = bytes([decrypter.decrypt(b) for b in encrypted_data])

print(f"[+] Decrypted: {len(decrypted)} bytes")
print(f"[+] Hex: {decrypted.hex()}")
```

### Step 5: Extract the Flag

Running the decryption script:

```
[+] Encrypted data: 52 bytes
[+] Decrypted: 52 bytes
[+] Hex: 2f6ac47e02c39fb907d90264626374667b6e6f745f616c6c5f6861736865735f6172655f6861736865645f657175616c6c797d0a
```

The first 12 bytes (`2f6ac47e02c39fb907d90264`) are the encryption header used for password verification.

The remaining 40 bytes contain our data. Since the compression method was `2` (stored, not compressed), we can directly read it:

```bash
echo "626374667b6e6f745f616c6c5f6861736865735f6172655f6861736865645f657175616c6c797d0a" | python3 -c "import sys; print(bytes.fromhex(sys.stdin.read().strip()).decode())"
```

Output:
```
bctf{not_all_hashes_are_hashed_equally}
```

**Flag:** `bctf{not_all_hashes_are_hashed_equally}`

---

## Key Takeaways

1. **pkzip2 hashes contain encrypted data:** Unlike password hashes, the pkzip2 format includes the actual encrypted file data, not just verification information.

2. **Compression method matters:** Field 2 being `2` indicated "stored" (no compression), so we didn't need to decompress after decryption.

3. **Traditional PKZIP encryption is cryptographically weak:** It uses a custom stream cipher that can be decrypted once you have the password, and the password can often be cracked with tools like John the Ripper.

4. **The challenge name was a hint:** "zip2john2zip" literally described the process:
   - `zip` → Some original ZIP file was created
   - `2john` → `zip2john` extracted the hash
   - `2zip` → We reverse the process to recover the data

5. **Trust the hash format:** All the information needed to recover the plaintext was embedded in the hash itself - no original ZIP file required!

---

## Tools Used

- **John the Ripper (Jumbo):** Password cracking
- **Python 3:** Custom PKZIP decryption implementation
- **rockyou.txt:** Password wordlist

---

## Complete Solution Script

Here's the complete Python script to solve this challenge:

```python
#!/usr/bin/env python3
"""
Complete solution for zip2john2zip CTF challenge
"""

class PKZIPDecrypter:
    def __init__(self, password):
        self.keys = [0x12345678, 0x23456789, 0x34567890]
        for c in password:
            self._update_keys(ord(c))
    
    def _update_keys(self, c):
        self.keys[0] = self._crc32(self.keys[0], c)
        self.keys[1] = (self.keys[1] + (self.keys[0] & 0xFF)) & 0xFFFFFFFF
        self.keys[1] = (self.keys[1] * 134775813 + 1) & 0xFFFFFFFF
        self.keys[2] = self._crc32(self.keys[2], self.keys[1] >> 24)
    
    def _crc32(self, crc, c):
        crc_table = []
        for i in range(256):
            c_val = i
            for j in range(8):
                if c_val & 1:
                    c_val = 0xEDB88320 ^ (c_val >> 1)
                else:
                    c_val = c_val >> 1
            crc_table.append(c_val)
        return crc_table[(crc ^ c) & 0xFF] ^ (crc >> 8)
    
    def decrypt(self, c):
        temp = self.keys[2] | 2
        c = c ^ (((temp * (temp ^ 1)) >> 8) & 0xFF)
        self._update_keys(c)
        return c

def main():
    # Read hash file
    with open('hash.txt', 'r') as f:
        hash_line = f.read().strip()
    
    # Parse pkzip2 hash
    parts = hash_line.split('$pkzip2$')
    fields = parts[1].split('*')
    
    encrypted_hex = fields[13]
    encrypted_data = bytes.fromhex(encrypted_hex)
    
    # Decrypt with cracked password
    password = "factfinder"  # Cracked with John the Ripper
    decrypter = PKZIPDecrypter(password)
    decrypted = bytes([decrypter.decrypt(b) for b in encrypted_data])
    
    # Skip 12-byte encryption header, get the data
    # (Compression method 2 = stored, no decompression needed)
    data = decrypted[12:]
    
    # Extract and display flag
    flag = data.decode('ascii').strip()
    print(f"Flag: {flag}")
    
    with open('flag.txt', 'w') as f:
        f.write(flag + '\n')
    print("Flag saved to flag.txt")

if __name__ == '__main__':
    main()
```

Run it:
```bash
python3 solve.py
```

Output:
```
Flag: bctf{not_all_hashes_are_hashed_equally}
Flag saved to flag.txt
```

---

## References

- [PKZIP Application Note (APPNOTE.TXT)](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) - Official ZIP format specification
- [John the Ripper](https://www.openwall.com/john/) - Password cracking tool
- [zip2john source code](https://github.com/openwall/john/blob/bleeding-jumbo/src/zip2john.c) - Understanding the hash format

---

**Author:** [Your Name]  
**Date:** November 2025  
**Challenge Source:** [CTF Name/Platform]
