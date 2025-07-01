with open("Project Euler/data/p22names.txt") as file:
    broken = []
    for line in file:
        broken.extend(line.split("\""))

names = sorted([broken[i] for i in range(1, len(broken), 2)])
score = 0

for i, name in enumerate(names):
    nameScore = 0
    for char in name:
        nameScore += ord(char) - 64
    score += nameScore * (i + 1)

print(score)