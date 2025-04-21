def solve(s):
    listed = list(s)
    indices = []
    vowels = []
    for i in range(len(s)):
        if s[i] in "aeiou":
            indices.append(i)
            vowels.append(s[i])
    vowels = vowels[::-1]
    for i in range(len(indices)):
        listed[indices[i]] = vowels[i]
    return "".join(listed)