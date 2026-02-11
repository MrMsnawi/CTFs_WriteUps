import telnetlib
from pwn import *
from sympy.ntheory.modular import crt
from sympy.ntheory import discrete_log
import random

# --- ECC Minimal Implementation ---
def inverse(a, n):
    return pow(a, -1, n)

def point_add(P, Q, a, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2: return None
    if x1 == x2:
        m = (3 * x1 * x1 + a) * inverse(2 * y1, p)
    else:
        m = (y2 - y1) * inverse(x2 - x1, p)
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(P, k, a, p):
    R = None
    while k > 0:
        if k % 2 == 1: R = point_add(R, P, a, p)
        P = point_add(P, P, a, p)
        k //= 2
    return R

# --- The Exploit ---
def solve():
    io = remote('curve.ctf.pascalctf.it', 5004)
    
    # Generic parsing - update based on 'nc' output
    io.recvuntil(b"p = ")
    p = int(io.recvline().strip())
    io.recvuntil(b"a = ")
    a = int(io.recvline().strip())
    
    remainders = []
    moduli = []
    current_prod = 1

    # We need enough small primes to reach ~2^256
    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for q in small_primes:
        # 1. Find a point on an invalid curve y^2 = x^3 + ax + b'
        # We pick a random x and y, then find what b' would make it valid
        found_point = False
        while not found_point:
            test_x = random.randint(1, p-1)
            test_y = random.randint(1, p-1)
            # b' = y^2 - x^3 - ax
            b_prime = (test_y**2 - test_x**3 - a*test_x) % p
            
            # This is the tricky part without Sage: finding the order of the curve.
            # For a "Small Subgroup Attack", we often just send points and see if it works.
            # But the 'oracle' needs to return a point.
            
            io.sendlineafter(b"> ", f"{test_x} {test_y}".encode())
            resp = io.recvline().decode()
            
            # Parse Q = d * P
            # Extract Qx, Qy from resp...
            # Then solve d_mod = discrete_log_brute_force(P, Q, q)
            
            # Note: This pure python version is significantly more complex to 
            # make robust. Sage is standard for this reason.
            break 

    print("This challenge is best solved with SageMath due to its point-counting capabilities.")

# solve()
