import csv

count = 0
primes = []
circular = []

with open("Project Euler/data/Primes Below 1 Million.csv") as file:
    csvReader = csv.reader(file)
    for line in csvReader:
        primes.extend(line)

print(primes)
print(primes[1], type(primes[1]))

for j, prime in enumerate(primes):
    if prime in circular:
        continue
    listed = list(str(prime))
    options = []
    for i in range(len(listed)):
        if int("".join(listed)) not in primes:
            break
        listed.append(listed.pop(0))
        options.append("".join(listed))
    else:
        count += 1
        circular.extend(options)
    if j % 1000 == 0:
        print(j)

print(len(primes))
print(count)