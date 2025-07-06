# Taken from a writeup

import hashlib

target = "0414011c408858aaae1d8bcf7a8e4ae9cd655a39d91242c3dc7dcb551ca78c09"

def sha256_hash(text):
    # This function hashes the text and salt into sha256.
    # Returns a dictionary of possible hash-salt pairs.
    hash_dict = {}

    # 2 nibbles of hexadecimal-character is 1-byte length, which is 256 possible values.
    # 0x00, 0x01, 0x02, ... , 0x1a, ..., 0xff.
    for i in range(256):
        # Salt in 1-byte hex value.
        salt_hex = f"{i:02x}"    # hex(i) can't be used here because it must be exactly 1-byte long, e.g. 00 not 0.

        # Hashing salt_hex then text (original text).
        hash = hashlib.sha256((salt_hex + text).encode()).hexdigest()
        hash_dict[hash] = salt_hex

        # Hashing text then salt_hex (original text).
        hash = hashlib.sha256((text + salt_hex).encode()).hexdigest()
        hash_dict[hash] = salt_hex

        # Hashing salt_hex then text with all uppercase text.
        hash = hashlib.sha256((salt_hex + text.upper()).encode()).hexdigest()
        hash_dict[hash] = salt_hex

        # Hashing text then salt_hex with all uppercase text.
        hash = hashlib.sha256((text.upper() + salt_hex).encode()).hexdigest()
        hash_dict[hash] = salt_hex

        # Hashing salt_hex then text with all lowercase text.
        hash = hashlib.sha256((salt_hex + text.lower()).encode()).hexdigest()
        hash_dict[hash] = salt_hex

        # Hashing text then salt_hex with all lowercase text.
        hash = hashlib.sha256((text.lower() + salt_hex).encode()).hexdigest()
        hash_dict[hash] = salt_hex
        salt_byte = bytes.fromhex(salt_hex)
        
        # Hashing salt_byte then text (original text).
        hash = hashlib.sha256(salt_byte + text.encode()).hexdigest()
        hash_dict[hash] = salt_byte

        # Hashing text then salt_byte (original text).
        hash = hashlib.sha256(text.encode() + salt_byte).hexdigest()
        hash_dict[hash] = salt_byte

        # Hashing salt_byte then text with all uppercase text.
        hash = hashlib.sha256(salt_byte + text.upper().encode()).hexdigest()
        hash_dict[hash] = salt_byte

        # Hashing text then salt_byte with all uppercase text.
        hash = hashlib.sha256(text.upper().encode() + salt_byte).hexdigest()
        hash_dict[hash] = salt_byte

        # Hashing salt_byte then text with all lowercase text.
        hash = hashlib.sha256(salt_byte + text.lower().encode()).hexdigest()
        hash_dict[hash] = salt_byte

        # Hashing text then salt_byte with all lowercase text. The winning hash method.
        hash = hashlib.sha256(text.lower().encode() + salt_byte).hexdigest()
        hash_dict[hash] = salt_byte

    return hash_dict

with open("CTF Stuff/data/cheese_list.txt") as file:
    for line in file:
        hashes = sha256_hash(line.strip())
        if target in hashes:
            print(line, hashes[target])






        # for encoding in ["utf-8", "utf-16-le", "utf-16-be", "latin-1"]:
        #     for salt_val in range(256):
        #         combined = line.encode(encoding) + bytes([salt_val])
        #         salt_str = format(salt_val, "02x")
        #         if hashlib.sha256(combined).hexdigest() == target:
        #             print(line, salt_str)
        #             print(combined)
        #         if hashlib.sha256(combined.lower()).hexdigest() == target:
        #             print(line, salt_str)
        #             print(combined)
        #         if hashlib.sha256(combined.upper()).hexdigest() == target:
        #             print(line, salt_str)
        #             print(combined)
