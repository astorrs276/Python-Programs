def solve(s1, s2):
    list1 = []
    for char in s1:
        list1.append(ord(char))
    list1.sort()
    list2 = []
    for char in s2:
        list2.append(ord(char))
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False