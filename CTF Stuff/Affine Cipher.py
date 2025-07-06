a = 1
b = 1

def encrypt(letter, a, b):
    return chr((a * (ord(letter) - 65) + b) % 26 + 65)

def decrypt(letter, a, b):
    for i in range(50):
        if a * i % 26 == 1:
            a2 = i
            break
    return chr(a2 * ((ord(letter) - 65) - b) % 26 + 65)

def find_keys(plain, cipher):
    global a, b
    found = False
    for i in range(50):
        if found:
            break
        for j in range(25):
            checked = ""
            for letter in plain.upper():
                checked += encrypt(letter, i, j)
            if checked == cipher.upper():
                print(i, j)
                a, b = i, j
                found = True
                break

find_keys("gouda", "SGKDO")
find_keys("mozzarella", "WGJJOVIRRO")

for letter in "OKFKBDCM":
    print(decrypt(letter, a, b), end="")
