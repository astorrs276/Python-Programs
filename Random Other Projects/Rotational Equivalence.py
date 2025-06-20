def check(num1, num2):
    return num2 in [num1[i:] + num1[:i] for i in range(len(num1))]

def main():
    while True:
        val = input("Enter two numbers (q = quit): ")
        if val == "q":
            break
        nums = val.split()
        print(check(nums[0], nums[1]))

if __name__ == "__main__":
    main()




# Original and much less efficient version
'''
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
'''