def solve(num_courses, prerequisites):
    prereqs = dict()
    for item in prerequisites:
        if item[1] not in prereqs:
            prereqs[item[1]] = []
        prereqs[item[1]].append(item[0])
    for key in prereqs:
        for item in prereqs[key]:
            if item in prereqs and key in prereqs[item]:
                return False
    return True