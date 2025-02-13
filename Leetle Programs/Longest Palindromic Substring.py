def solve(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            if (temp == temp[::-1]) and (j - i > len(longest)):
                longest = s[i:j]
    return longest