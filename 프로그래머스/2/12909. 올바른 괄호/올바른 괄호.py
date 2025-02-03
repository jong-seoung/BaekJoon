def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if stack.pop() == '(':
                pass
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False