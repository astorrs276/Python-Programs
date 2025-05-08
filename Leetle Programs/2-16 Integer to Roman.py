def solve(num):
    smalls = str(num % 1000)[::-1]
    thousands = num // 1000
    roman = ""
    ones = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
    tens = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
    hundreds = {'0':'', '1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM'}
    for i, char in enumerate(smalls):
        if i == 0:
            roman = ones[char] + roman
        elif i == 1:
            roman = tens[char] + roman
        elif i == 2:
            roman = hundreds[char] + roman
    roman = "".join(['M' for _ in range(thousands)]) + roman
    return roman