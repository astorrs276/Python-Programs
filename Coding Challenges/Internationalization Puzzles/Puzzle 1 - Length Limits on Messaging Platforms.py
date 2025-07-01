def check_bytes(string):
    return len(string.encode("utf-8")) <= 160

def check_characters(string):
    return len(string) <= 140

cost = 0

with open("Internationalization Puzzles/data/puzzle1.txt", "r", encoding="utf-8") as file:
    for line in file:
        stripped_line = line.strip()
        sms_safe = check_bytes(stripped_line)
        tweet_safe = check_characters(stripped_line)
        if sms_safe and tweet_safe:
            cost += 13
        elif sms_safe and not tweet_safe:
            cost += 11
        elif not sms_safe and tweet_safe:
            cost += 7

print(cost)