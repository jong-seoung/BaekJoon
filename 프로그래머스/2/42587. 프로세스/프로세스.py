def solution(priorities, location):
    answer = 0
    res = []
    while len(priorities) > 0:
        M = max(priorities)
        queue = priorities.pop(0)
        location -= 1
        print(M, res, queue, priorities, location)
        if M != queue:
            priorities.append(queue)
            if location == -1:
                location = len(priorities) - 1
        else:
            res.append(queue)
            if location == -1:
                return len(res)