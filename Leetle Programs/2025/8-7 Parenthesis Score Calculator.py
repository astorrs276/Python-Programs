def solve(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                score = 0
                while stack[-1] != '(':
                    score += stack.pop()
                stack.pop()
                stack.append(2 * score)
    return sum(stack)