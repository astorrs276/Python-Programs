def encrypt(text, shift):
    return "".join([chr((ord(char) - 65 + shift) % 26 + 65) if 65 <= ord(char) <= 90 else chr((ord(char) - 97 + shift) % 26 + 97) if 97 <= ord(char) <= 122 else char for char in text])

def decrypt(text, shift):
    return "".join([chr((ord(char) - 65 - shift) % 26 + 65) if 65 <= ord(char) <= 90 else chr((ord(char) - 97 - shift) % 26 + 97) if 97 <= ord(char) <= 122 else char for char in text])

def brute_decrypt(text):
    return "\n".join([decrypt(text, i) for i in range(26)])

def main():
    while True:
        type = input("Encrypt or decrypt (q = quit)? ").lower()
        if type == "q":
            break
        text = input("Enter the message: ")
        shift = input("Enter the shift (leave blank for brute force decrypt): ")
        print(encrypt(text, int(shift)) if type == "e" else brute_decrypt(text) if shift == "" else decrypt(text, int(shift)))
        print()

if __name__ == "__main__":
    main()




# Original and much less efficient version
'''
def is_uppercase(character):
    pos = ord(character)
    if (pos >= 65 and pos <= 90):
        return True
    else:
        return False

def is_lowercase(character):
    pos = ord(character)
    if (pos >= 97 and pos <= 122):
        return True
    else:
        return False

def encrypt_letter(letter, shift=3):
    ind = ord(letter)
    ind = ind + shift
    if (is_uppercase(letter)):
        while (ind > 90):
            ind = ind - 26
        char = chr(ind)
        return char
    elif (is_lowercase(letter)):
        while (ind > 122):
            ind = ind - 26
        char = chr(ind)
        return char
    else:
        return letter

def decrypt_letter(letter, shift=3):
    ind = ord(letter)
    ind = ind - shift
    if (is_uppercase(letter)):
        while (ind < 65):
            ind = ind + 26
        char = chr(ind)
        return char
    elif (is_lowercase(letter)):
        while (ind < 97):
            ind = ind + 26
        char = chr(ind)
        return char
    else:
        return letter

def encrypt_message(message, shift=3):
    ciphertext = ""
    for i in range (len(message)):
        ciphertext = ciphertext + str(encrypt_letter(message[i], shift))
    return ciphertext

def decrypt_message(message, shift=3):
    plaintext = ""
    for i in range (len(message)):
        plaintext = plaintext + str(decrypt_letter(message[i], shift))
    return plaintext

def main():
    word = input("Enter a word: ")
    change = int(input("How much to shift? "))
    encrypted = encrypt_message(word, change)
    print(encrypted)
    decrypted = decrypt_message(encrypted, change)
    print(decrypted)

if (__name__ == "__main__"):
    main()
'''