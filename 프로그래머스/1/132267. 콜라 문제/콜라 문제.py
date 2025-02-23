def solution(a, b, n):
    answer = 0
    
    while (n) >= a:
        remain = 0
        remain = n % a
        n = (n // a) * b
        answer += n
        n += remain
        
    return answer