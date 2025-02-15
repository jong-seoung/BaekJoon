def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(i)
    answer.sort(reverse=True)
    
    a = ''.join(answer)
    return int(a)