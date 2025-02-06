def solution(priorities, location):
    answer = 0
    ans = []
    while len(priorities) > 0:
        max_pri = max(priorities)
        queue = priorities.pop(0)
        location -= 1
        print(ans, max_pri, queue, location)
        if max_pri == queue:
            ans.append(queue)
            if location == -1:
                return len(ans) 
        else:
            priorities.append(queue)
        
        if location == -1:
            location = len(priorities) - 1
    return len(ans)