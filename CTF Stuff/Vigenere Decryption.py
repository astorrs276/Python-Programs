def find_vigenere_key(plaintext, ciphertext):
    key = []
    for p, c in zip(plaintext.upper(), ciphertext.upper()):
        if p.isalpha() and c.isalpha():
            shift = (ord(c) - ord(p)) % 26
            key.append(chr(ord('A') + shift))
    key_str = ''.join(key)
    for i in range(1, len(key_str)):
        if (key_str[:i] * (len(key_str) // i + 1))[:len(key_str)] == key_str:
            return key_str[:i]
    return key_str

print(find_vigenere_key("", ""))
