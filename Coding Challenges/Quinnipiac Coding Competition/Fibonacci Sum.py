fibonacci = [1, 1]

def expand_fibonacci(x):
    global fibonacci
    while fibonacci[-1] + fibonacci[-2] <= x:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

def get_sum(x):
    global fibonacci
    if fibonacci[-1] + fibonacci[-2] <= x:
        expand_fibonacci(x)
    result = []
    current = x
    for i in range(len(fibonacci) - 1, -1, -1):
        if fibonacci[i] <= current:
            current -= fibonacci[i]
            result.append(fibonacci[i])
            if current == 0:
                return result

def main():
    while True:
        x = input("Enter a number (q = quit): ")
        if x.lower() == "q":
            break
        print(get_sum(int(x)))

if __name__ == "__main__":
    main()




# Original and much less efficient version
'''
def findNumbers2(fibList, inp):
    numbers = []
    inp2 = inp
    for i in range(len(fibList)):
        if(inp == fibList[i]):
            numbers.append(inp)
            return numbers

    while (inp2 > 0):
        for j in range(len(fibList)):
            if(inp2 == fibList[j]):
                numbers.append(fibList[j])
                numbers.sort()
                return numbers
            elif(inp2 < fibList[j]):
                numbers.append(fibList[j - 1])
                inp2 = inp2 - fibList[j - 1]
                for k in range(len(fibList) - 1, j, -1):
                    fibList.remove(fibList[k])
                    fibList.insert(k, 0)

x = int(input("Enter a number: "))

fibonacci = [1, 1]
a = 1
b = 1
while(x > a):
    temp = a
    a = a + b
    b = temp
    fibonacci.append(a)

print(findNumbers2(fibonacci, x))
'''