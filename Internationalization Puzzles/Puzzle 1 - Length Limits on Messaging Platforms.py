def check_bytes(string):
    return len(string.encode("utf-8")) <= 160

def check_characters(string):
    return len(string) <= 140

cost = 0
with open("Internationalization Puzzles/data/test.txt") as file:
    for line in file:
        sms_safe = check_bytes(line)
        tweet_safe = check_characters(line)
        if sms_safe and tweet_safe:
            cost += 13
        elif sms_safe and not tweet_safe:
            cost += 11
        elif not sms_safe and tweet_safe:
            cost += 7

print(cost)