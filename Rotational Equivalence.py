first = ""
second = ""
listed = []
rotated = ""
success = False

def rotate():
    global listed
    global rotated
    temp = listed[0]
    listed.append(temp)
    listed.pop(0)
    rotated = ""
    for i in range(len(listed)):
        rotated = rotated + str(listed[i])
    return listed
    return rotated

def main():
    global listed
    global success
    global rotated
    first = str(input("Enter a number: "))
    second = str(input("Enter another number: "))
    listed = [*first]
    a = len(first)

    for i in range(len(first)):
        if (rotated == second):
            success = True
        rotate()

    if (success):
        print("YES! These numbers are rotationally equivalent.")
    else:
        print("NO. These numbers are not rotationally equivalent")

    return listed
    return success
    return rotated

main()