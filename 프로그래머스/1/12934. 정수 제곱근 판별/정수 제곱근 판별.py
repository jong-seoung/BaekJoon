import math 

def solution(n):
    answer = 0
    num = n ** (1/2)
    
    if n == math.ceil(num) ** 2:
        return (num+1) **2
    else:
        return -1
    return answer