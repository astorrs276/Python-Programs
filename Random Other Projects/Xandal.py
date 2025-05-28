# The Xandalizer V1.1.1
import random

definition = '''Xandal (verb)
zan-dull

See also - Xandalize

To try to complete every item on the following list

To Note:
Can be used in place of any other verb
'''

xandalist = [
    'Get Xander to say he is xandaling/xandalizing',
    'Get Xander to guess it means something related to cumming',
    'Get Xander to agree that he is crazy and xandalizing isnt a thing',
    'Get Xander to be genuinely wierded out by the term xandalizing',
]

def xandler():
    r = random.randint(0, len(xandalist) - 1)
    return r

def main():
    print(definition)
    print("Todo:")
    for item in xandalist:
        print(" - " + item)
    while True:
        print()
        guypt2 = input('byebye? (y/n): ')
        if guypt2 == 'y':
            break
        r = xandler()
        print(xandalist[r])
        theguy = input('you complete this? (y/n): ')
        if theguy == 'y':
            xandalist.pop(r)
            if len(xandalist) == 0:
                print("\nyou got them all!")
                break

if __name__ == "__main__":
    main()