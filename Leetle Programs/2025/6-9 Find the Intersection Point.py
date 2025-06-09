def solve(list1, list2):
    return [list1[i] for i in range(len(list1)) if list1[i] in list2 and list1[i] not in list1[:i]]