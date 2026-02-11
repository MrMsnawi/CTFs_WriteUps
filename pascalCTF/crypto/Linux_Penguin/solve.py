#!/usr/bin/env python3
"""
Penguin Challenge Solver - Final Solution
"""

import socket
import re
import time

words = [
    "biocompatibility", "biodegradability", "characterization", "contraindication",
    "counterbalancing", "counterintuitive", "decentralization", "disproportionate",
    "electrochemistry", "electromagnetism", "environmentalist", "internationality",
    "internationalism", "institutionalize", "microlithography", "microphotography",
    "misappropriation", "mischaracterized", "miscommunication", "misunderstanding",
    "photolithography", "phonocardiograph", "psychophysiology", "rationalizations",
    "representational", "responsibilities", "transcontinental", "unconstitutional"
]

def recv_until(sock, pattern, timeout=10, debug=False):
    sock.settimeout(timeout)
    data = b""
    pattern_bytes = pattern.encode() if isinstance(pattern, str) else pattern
    
    try:
        while pattern_bytes not in data:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            if debug and chunk:
                print(f"[DEBUG] Chunk: {chunk[:200].decode('utf-8', errors='ignore')}")
    except socket.timeout:
        if debug:
            print(f"[DEBUG] Timeout waiting for: {pattern}")
    
    return data

def send_line(sock, line, debug=False):
    if isinstance(line, str):
        line = line.encode()
    if not line.endswith(b'\n'):
        line += b'\n'
    if debug:
        print(f"[SEND] {line.decode().strip()}")
    sock.sendall(line)
    time.sleep(0.1)

def extract_hex_words(text):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'Encrypted words:' in line:
            after_colon = line.split('Encrypted words:')[1].strip()
            if after_colon:
                words_list = after_colon.split()
                if all(len(w) == 32 and all(c in '0123456789abcdefABCDEF' for c in w) for w in words_list):
                    return words_list
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                words_list = next_line.split()
                if all(len(w) == 32 and all(c in '0123456789abcdefABCDEF' for c in w) for w in words_list):
                    return words_list
    return None

def exploit_remote(debug=False):
    HOST = "penguin.ctf.pascalctf.it"
    PORT = 5003
    
    print(f"[+] Connecting to {HOST}:{PORT}")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        return None
    
    print("[+] Connected!")
    
    time.sleep(0.3)
    initial = recv_until(sock, "Word 1:", timeout=5, debug=debug)
    
    if b"Welcome" in initial:
        print("[+] Banner received!")
    
    encryption_dict = {}
    print("[+] Building encryption oracle dictionary...\n")
    
    word_chunks = [words[i:i+4] for i in range(0, len(words), 4)]
    
    # Variable to store Round 7 response which contains the challenge
    round7_full_response = ""
    
    for round_num, chunk in enumerate(word_chunks):
        if round_num >= 7:
            break
        
        print(f"[Round {round_num + 1}]")
        
        try:
            for j, word in enumerate(chunk):
                if not (round_num == 0 and j == 0):
                    recv_until(sock, f"Word {j+1}:", timeout=3, debug=debug)
                send_line(sock, word, debug=debug)
            
            # For Round 7, we need to wait longer because the challenge comes right after
            if round_num == 6:
                time.sleep(0.8)  # Give extra time for the full challenge to arrive
            else:
                time.sleep(0.2)
            
            sock.setblocking(False)
            try:
                response = b""
                attempts = 0
                while attempts < 20:  # Try multiple times to get all data
                    try:
                        chunk_data = sock.recv(4096)
                        if chunk_data:
                            response += chunk_data
                            attempts = 0  # Reset if we got data
                        else:
                            break
                    except BlockingIOError:
                        attempts += 1
                        time.sleep(0.05)  # Small delay between attempts
            finally:
                sock.setblocking(True)
            
            response_text = response.decode('utf-8', errors='ignore')
            
            if round_num == 6:
                round7_full_response = response_text  # Save for later
            
            if debug:
                print(f"[DEBUG] Response ({len(response_text)} chars):\n{response_text[:400]}")
            
            encrypted_words = extract_hex_words(response_text)
            
            if not encrypted_words:
                print(f"  [!] Could not parse encrypted words")
                continue
            
            for word, encrypted in zip(chunk, encrypted_words):
                encryption_dict[encrypted] = word
                print(f"  {word[:22]:22} -> {encrypted[:16]}...")
        
        except Exception as e:
            print(f"  [-] Error: {e}")
            if debug:
                import traceback
                traceback.print_exc()
            sock.close()
            return None
    
    print(f"\n[+] Dictionary complete: {len(encryption_dict)} entries\n")
    
    # Extract ciphertext from Round 7 response
    print("[+] Extracting challenge from Round 7 response...")
    
    if debug:
        print(f"[DEBUG] Round 7 full response:\n{round7_full_response}")
    
    lines = round7_full_response.split('\n')
    ciphertext_line = None
    
    for i, line in enumerate(lines):
        if 'Ciphertext:' in line:
            # Get everything after "Ciphertext:"
            after_colon = line.split('Ciphertext:')[1].strip()
            if after_colon and len(after_colon) > 50:
                ciphertext_line = after_colon
                break
            # Try next line
            elif i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and len(next_line) > 50:
                    ciphertext_line = next_line
                    break
    
    if not ciphertext_line:
        print(f"[-] Could not find ciphertext in Round 7 response")
        if debug:
            print(f"[DEBUG] Available lines:")
            for i, line in enumerate(lines[:20]):
                print(f"  [{i}] {line[:100]}")
        sock.close()
        return None
    
    print(f"  Ciphertext ({len(ciphertext_line)} chars): {ciphertext_line}\n")
    
    # Decrypt
    target_ciphertexts = ciphertext_line.split()
    
    print(f"[+] Found {len(target_ciphertexts)} target ciphertexts")
    print(f"[+] Decrypting...\n")
    
    decrypted_words = []
    for i, ct in enumerate(target_ciphertexts):
        if ct in encryption_dict:
            word = encryption_dict[ct]
            decrypted_words.append(word)
            print(f"  [{i+1}] {ct[:16]}... -> {word}")
        else:
            print(f"  [{i+1}] NOT FOUND: {ct}")
            if debug:
                print(f"[DEBUG] Dictionary has {len(encryption_dict)} entries")
                print(f"[DEBUG] Sample keys: {list(encryption_dict.keys())[:3]}")
            sock.close()
            return None
    
    # Submit
    print(f"\n[+] Submitting answers...\n")
    for i, word in enumerate(decrypted_words):
        try:
            recv_until(sock, f"Guess the word {i+1}:", timeout=3, debug=debug)
            send_line(sock, word, debug=debug)
            print(f"  [{i+1}] {word}")
            
            time.sleep(0.2)
            sock.setblocking(False)
            try:
                response = sock.recv(1024).decode('utf-8', errors='ignore')
                if "Wrong" in response:
                    print(f"       ✗ Wrong!")
                    sock.close()
                    return None
                elif "Correct" in response:
                    print(f"       ✓ Correct!")
            except BlockingIOError:
                pass
            finally:
                sock.setblocking(True)
        except Exception as e:
            print(f"  [-] Error: {e}")
    
    # Get flag
    print(f"\n[+] Getting flag...\n")
    time.sleep(0.5)
    
    try:
        sock.setblocking(False)
        flag_data = b""
        try:
            for _ in range(10):
                try:
                    chunk_data = sock.recv(4096)
                    if chunk_data:
                        flag_data += chunk_data
                except BlockingIOError:
                    time.sleep(0.1)
        finally:
            sock.setblocking(True)
        
        flag_text = flag_data.decode('utf-8', errors='ignore')
        
        print('='*70)
        print(flag_text)
        print('='*70)
        
        flag_match = re.search(r'pascalCTF\{[^}]+\}', flag_text)
        if flag_match:
            sock.close()
            return flag_match.group(0)
    except Exception as e:
        print(f"[-] Error getting flag: {e}")
    
    sock.close()
    return None

def main():
    import sys
    
    debug = '--debug' in sys.argv or '-d' in sys.argv
    
    print("="*70)
    print("Penguin Challenge - AES ECB Oracle Attack")
    print("="*70)
    print()
    
    if debug:
        print("[DEBUG MODE ENABLED]\n")
    
    try:
        flag = exploit_remote(debug=debug)
        
        if flag:
            print(f"\n🚩 FLAG: {flag}\n")
            print('='*70)
        else:
            print("\n[-] Failed to get flag")
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted")
    except Exception as e:
        print(f"\n[-] Error: {e}")
        if debug:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
