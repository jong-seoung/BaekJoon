def solution(s):
    answer = True
    queue = []
    
    for i in s:
        if len(queue) == 0 and i == ')':
            answer = False
            break
        elif i == ')':
            if queue.pop() != '(':
                answer=False
                break
        else:
            queue.append(i)

    if len(queue) != 0:
        answer = False
    return answer