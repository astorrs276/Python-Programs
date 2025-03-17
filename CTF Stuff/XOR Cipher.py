def xor_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    # Decrypts repeating key XOR ciphertext using the key
    return bytes(c ^ key[i % len(key)] for i, c in enumerate(ciphertext))

def recover_repeating_key(ciphertext: bytes, known_plaintext: bytes) -> bytes:
    # Recovers the key by XORing plaintext and ciphertext
    key_guess = bytes(c ^ p for c, p in zip(ciphertext[:len(known_plaintext)], known_plaintext))
    return key_guess

ciphertext_hex = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
ciphertext = bytes.fromhex(ciphertext_hex)

known_plaintext = b"ORDER:"

key = recover_repeating_key(ciphertext, known_plaintext)
print("Key:", key)

plaintext = xor_decrypt(ciphertext, key)
print("Decrypted Text:", plaintext.decode(errors="ignore"))
