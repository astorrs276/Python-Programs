import re

strings = ["112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 51 100 56 52 101 100 99 56 125 10", # picoCTF - Nice netcat...
            ]
listed = [int(n) for n in re.findall(r'\d+', strings[-1])]

for item in listed:
    print(chr(item), end="")