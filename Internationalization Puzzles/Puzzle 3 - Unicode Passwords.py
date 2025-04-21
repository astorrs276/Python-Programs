import unicodedata as ucd

def check_length(password):
    return len(password) >= 4 and len(password) <= 12

def check_digit(password):
    return any(digit in password for digit in "1234567890")

def check_upper(password):
    return any((('WITH' in ucd.name(char, '') and char.isupper()) or char.isupper()) for char in password if char.isalpha())

def check_lower(password):
    return any((('WITH' in ucd.name(char, '') and char.islower()) or char.islower()) for char in password if char.isalpha())

def check_outside_7_bit_ascii(password):
    return any(ord(char) > 127 for char in password)

def check_all(password):
    return check_length(password) and check_digit(password) and check_upper(password) and check_lower(password) and check_outside_7_bit_ascii(password)

valid = 0

with open("Internationalization Puzzles/data/puzzle3.txt", encoding="utf-8") as file:
    for line in file:
        stripped_line = line.strip()
        if check_all(stripped_line):
            valid += 1

print(valid)