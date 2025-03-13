from itertools import combinations

def solution(nums):
    res = []
    answer = 0
    
    for i in combinations(nums, 3):
        res.append(sum(i))

    for i in res:
        r = 1
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                r = 0
                break
        if r:
            answer += 1
            
    return answer