def egcd(a, b):
    """Extended Euclidean Algorithm to find modular inverse"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    """Modular inverse using EEA"""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def long_to_bytes(n):
    """Converts a long integer to a byte string"""
    result = bytearray()
    while n > 0:
        result.insert(0, n & 0xFF)
        n >>= 8
    return bytes(result)

# Given RSA values
n = 19112630570214557331109366330510811712077772794125325599771660275226838488937180782088322167280291699661919711250548912023801868417521003613389601403598034
e = 65537
ciphertext = 9770453172510761075168254840551289030313071075339207533028482417141369034236016803994267479611820614454821103699689304640950073927372874547979247684578827

# Replace with actual p and q
p = 143806475801846818371946446628872153612699240150586507753604931362184229013759
q = 58957103639008983646109338946521603421361629047078564077558515025698855777061

# Compute private key
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

# Decrypt
plaintext_num = pow(ciphertext, d, n)
plaintext = long_to_bytes(plaintext_num)

print("Decrypted plaintext:", plaintext.decode())
print("Raw bytes:", plaintext)
print("Hex     :", plaintext.hex())
