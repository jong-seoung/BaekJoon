def solution(a, b):
    answer = 0
    M = max(a,b)
    N = min(a,b)
    
    for i in range(N, M+1):
        answer += i
    return answer