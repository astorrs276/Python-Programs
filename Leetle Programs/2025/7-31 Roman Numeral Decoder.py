def solve(roman):
    value = 0
    i = 0
    while i < len(roman) - 1:
        if roman[i] == "M":
            value += 1000
            i += 1
        elif roman[i] == "D":
            value += 500
            i += 1
        elif roman[i] == "C":
            if roman[i + 1] == "M":
                value += 900
                i += 2
            elif roman[i + 1] == "D":
                value += 400
                i += 2
            else:
                value += 100
                i += 1
        elif roman[i] == "L":
            value += 50
            i += 1
        elif roman[i] == "X":
            if roman[i + 1] == "C":
                value += 90
                i += 2
            elif roman[i + 1] == "L":
                value += 40
                i += 2
            else:
                value += 10
                i += 1
        elif roman[i] == "V":
            value += 5
            i += 1
        elif roman[i] == "I":
            if roman[i + 1] == "X":
                value += 9
                i += 2
            elif roman[i + 1] == "V":
                value += 4
                i += 2
            else:
                value += 1
                i += 1
    if i < len(roman):
        value += 1
    return value