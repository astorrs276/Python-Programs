def solve(s):
    def check(i, count):
        if i >= len(s):
            return 0
        if s[i] != "0":
            if s[i:i + 2] == "10":
                return max(count, check(i + 2, count))
            elif 11 <= int(s[i:i + 2]) <= 26:
                try:
                    if s[i + 2] == "0":
                        count -= 1
                except:
                    pass
                count += 1
        return max(count, check(i + 1, count))
    return 0 if s == "" or s[0] == "0" else check(0, 1)