def get_fibonacci(x):
    fib = [1, 1]
    while fib[-1] + fib[-2] <= x:
        fib.append(fib[-1] + fib[-2])
    return fib

def get_sum(x):
    fib = get_fibonacci(x)
    result = []
    current = x
    for i in range(len(fib) - 1, -1, -1):
        if fib[i] <= current:
            current -= fib[i]
            result.append(fib[i])
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