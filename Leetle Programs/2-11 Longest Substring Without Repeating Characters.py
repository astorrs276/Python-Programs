def solve(s):
    max = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) == len(set(s[i:j])):
                if j - i > max:
                    max = j - i
    return max