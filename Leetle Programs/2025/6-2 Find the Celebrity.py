def solve(n, knows_data):
    # knows_data is a list of [a, b, result] where result is True if a knows b
    # This is a simulation of the knows() API - in a real interview, you'd have a knows(a, b) function
    knows_dict = {(a, b): result for a, b, result in knows_data}
    def knows(a, b):
        return knows_dict.get((a, b), False)

    for i in range(n):
        if all(True if i == j else knows(j, i) for j in range(n)):
            if not any(False if i == j else knows(i, j) for j in range(n)):
                return i
    return -1