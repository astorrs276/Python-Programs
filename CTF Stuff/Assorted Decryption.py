# Decryption based on given encryption function
'''
message = "a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm"

def enc(plaintext):
    return "".join(
        chr((ord(c) - (base := ord('A') if c.isupper() else ord('a')) + i) % 26 + base) 
        if c.isalpha() else c
        for i, c in enumerate(plaintext)
    )

def dec(ciphertext):
    return "".join(
        chr((ord(c) - (base := ord('A') if c.isupper() else ord('a')) - i) % 26 + base) 
        if c.isalpha() else c
        for i, c in enumerate(ciphertext)
    )

print(dec(message))
'''

# RSA Decryption
'''
import math

# Given RSA parameters
n = 196603733802071409961275562212278242151
e = 65537
c = 151832817966710307438243645623410737448

# Step 1: Factorize n to find p and q
def factorize_n(n):
    # Check for smallest factors up to the square root of n
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("Failed to factorize n.")

p, q = 879421070503884397, 223560408541749867683
print(f"Factors of n: p = {p}, q = {q}")

# Step 2: Compute the private exponent d
phi_n = (p - 1) * (q - 1)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi_n):
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("e and phi_n are not coprime.")
    return x % phi_n

d = mod_inverse(e, phi_n)
print(f"Private exponent d: {d}")

# Step 3: Decrypt the ciphertext c
m = pow(c, d, n)
print(f"Decrypted message (as integer): {m}")

# Convert the integer message to bytes
message_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
try:
    # Attempt to decode the bytes to a string
    message = message_bytes.decode()
except UnicodeDecodeError:
    # If decoding fails, print the bytes
    message = message_bytes
print(f"Decrypted message: {message}")
'''