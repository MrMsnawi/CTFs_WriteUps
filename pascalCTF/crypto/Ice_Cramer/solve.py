#!/usr/bin/env python3
"""
Automated solver for the Cramer challenge
Connects to the server, retrieves equations, and solves them
"""

import socket
import numpy as np
import re

def connect_and_get_equations(host, port):
    """Connect to the server and retrieve the equations"""
    print(f"[+] Connecting to {host}:{port}...")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((host, port))
        
        # Receive all data
        data = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            # Check if we received the complete output
            if b"Solve the system" in data:
                break
        
        sock.close()
        
        equations_text = data.decode('utf-8', errors='ignore')
        print("[+] Equations received!")
        return equations_text
    
    except Exception as e:
        print(f"[-] Connection error: {e}")
        return None

def parse_equations(equations_text):
    """Parse the system of equations into coefficient matrix A and result vector b"""
    lines = [line.strip() for line in equations_text.strip().split('\n') if '=' in line]
    
    if not lines:
        print("[-] No equations found!")
        return None, None
    
    # Determine the number of variables from the first equation
    first_eq = lines[0].split('=')[0]
    num_vars = len(re.findall(r'x_\d+', first_eq))
    
    print(f"[+] Found {len(lines)} equations with {num_vars} variables")
    
    A = []
    b = []
    
    for line in lines:
        # Split equation into left side (coefficients) and right side (result)
        left, right = line.split('=')
        
        # Parse the result
        result = int(right.strip())
        b.append(result)
        
        # Parse coefficients
        coefficients = [0] * num_vars
        
        # Find all terms like "coefficient*x_index"
        terms = re.findall(r'([+-]?\s*\d+)\s*\*\s*x_(\d+)', left)
        
        for coef, var_idx in terms:
            coef = int(coef.replace(' ', ''))
            var_idx = int(var_idx)
            coefficients[var_idx] = coef
        
        A.append(coefficients)
    
    return np.array(A, dtype=float), np.array(b, dtype=float)

def solve_system(A, b):
    """Solve the system of linear equations Ax = b"""
    print("[+] Solving the system...")
    try:
        # Using least squares for potentially overdetermined system
        x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        print(f"[+] Solution found! (rank={rank}, residuals={residuals})")
        return x
    except np.linalg.LinAlgError as e:
        print(f"[-] Error: System cannot be solved! {e}")
        return None

def decode_flag(solution):
    """Convert the solution (ASCII values) to the flag string"""
    # Round to nearest integer and convert to characters
    ascii_values = [int(round(val)) for val in solution]
    flag_chars = ''.join(chr(val) for val in ascii_values)
    return f"pascalCTF{{{flag_chars}}}"

def main():
    HOST = "cramer.ctf.pascalctf.it"
    PORT = 5002
    
    print("=" * 70)
    print("Cramer's Ice Cream Challenge - Automated Solver")
    print("=" * 70)
    
    # Connect and get equations
    equations_text = connect_and_get_equations(HOST, PORT)
    
    if not equations_text:
        print("[-] Failed to retrieve equations from server")
        print("[!] You can also paste equations manually:")
        print("    cat equations.txt | python solver.py")
        return
    
    # Parse the equations
    A, b = parse_equations(equations_text)
    
    if A is None or b is None:
        print("[-] Failed to parse equations!")
        return
    
    # Solve the system
    solution = solve_system(A, b)
    
    if solution is None:
        return
    
    # Decode the flag
    flag = decode_flag(solution)
    
    print("\n" + "=" * 70)
    print(f"🚩 FLAG: {flag}")
    print("=" * 70)
    
    # Show the ASCII values for verification
    print("\n[+] ASCII values:")
    ascii_values = [int(round(val)) for val in solution]
    print(ascii_values)
    print("\n[+] Characters:")
    print(''.join(chr(val) for val in ascii_values))

if __name__ == "__main__":
    main()
