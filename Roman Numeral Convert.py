def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
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

# Very inefficient code from original version
'''
num = 0
number_list = []
number_list_thousands = []
reversed = []
output_list = []
output_list_reversed = []
final = ""

def convert_thousands():
    length = ""
    for i in range (len(number_list_thousands)):
        length = length + number_list_thousands[i]
    length = int(length)
    for i in range (length):
        output_list.append("M")
    

def convert_hundreds():
    if (reversed[2] == 4):
        output_list.append("D")
        output_list.append("C")
    elif (reversed[2] == 9):
        output_list.append("M")
        output_list.append("C")

    if (reversed[2] >= 1 and reversed[2] <= 3):
        for i in range (int(reversed[2])):
            output_list.append("C")
    elif (reversed[2] >= 6 and reversed[2] <= 8):
        for i in range (int(reversed[2]) - 5):
            output_list.append("C")

    if (reversed[2] >= 5 and reversed[2] != 9):
        output_list.append("D")

def convert_tens():
    if (reversed[1] == 4):
        output_list.append("L")
        output_list.append("X")
    elif (reversed[1] == 9):
        output_list.append("C")
        output_list.append("X")

    if (reversed[1] >= 1 and reversed[1] <= 3):
        for i in range (int(reversed[1])):
            output_list.append("X")
    elif (reversed[1] >= 6 and reversed[1] <= 8):
        for i in range (int(reversed[1]) - 5):
            output_list.append("X")

    if (reversed[1] >= 5 and reversed[1] != 9):
        output_list.append("L")

def convert_ones():
    if (reversed[0] == 4):
        output_list.append("V")
        output_list.append("I")
    elif (reversed[0] == 9):
        output_list.append("X")
        output_list.append("I")

    if (reversed[0] >= 1 and reversed[0] <= 3):
        for i in range (int(reversed[0])):
            output_list.append("I")
    if (reversed[0] >= 6 and reversed[0] <= 8):
        for i in range (int(reversed[0]) - 5):
            output_list.append("I")

    if (reversed[0] >= 5 and reversed[0] != 9):
        output_list.append("V")


def main():
    global num
    global number_list
    global number_list_thousands
    global reversed
    global output_list
    global output_list_reversed
    global final

    num = str(input("Please enter a number: "))
    number_list = [char for char in num]
    for i in range (len(number_list) - 1, -1, -1):
        reversed.append(number_list[i])
    if (len(number_list) >= 4):
        for i in range (len(number_list) - 3):
            number_list_thousands.append(number_list[i])
    for i in range (len(reversed)):
        reversed[i] = int(reversed[i])

    if (len(reversed) >= 1):
        convert_ones()
        if (len(reversed) >= 2):
            convert_tens()
            if (len(reversed) >= 3):
                convert_hundreds()
                if (len(reversed) >= 4):
                    convert_thousands()

    for i in range(len(output_list) - 1, -1, -1):
        output_list_reversed.append(output_list[i])
    for i in range(len(output_list_reversed)):
        final = final + str(output_list_reversed[i])
    print(final)


main()
'''