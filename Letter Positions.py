letters = dict()
words = []

for i in range(97, 123):
    letters[chr(i)] = [0 for _ in range(5)]

with open('data/words.txt') as file:
    for line in file:
        words.append(line.strip())

for word in words:
    for i in range(len(word)):
        letters[word[i].lower()][i] += 1

for key in letters:
    print(key, "", letters[key])