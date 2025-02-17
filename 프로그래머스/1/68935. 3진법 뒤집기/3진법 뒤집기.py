def solution(n):
    answer = 0
    q = []
    
    while n > 0:
        q.append(n % 3)
        n = n // 3 
    q.reverse()
    
    for idx, i in enumerate(q):
        answer += (3**idx) * i
        
        
    return answer