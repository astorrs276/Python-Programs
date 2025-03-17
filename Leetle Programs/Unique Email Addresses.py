def solve(emails):
    uniques = set()
    for email in emails:
        at_break = email.split("@")
        front = at_break[0].split("+")[0]
        beginning = "".join(front.split("."))
        uniques.add(beginning + "@" + at_break[1])
    return len(uniques)