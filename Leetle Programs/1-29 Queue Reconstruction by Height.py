def solve(people):
    def sort_key(x):
        return -x[0], x[1]
    people = sorted(people, key=sort_key)
    queue = []
    for person in people:
        queue.insert(person[1], person)
    return queue