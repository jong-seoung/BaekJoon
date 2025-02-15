def solution(x):
    answer = True
    s = 0
    for i in str(x):
        s += int(i)
    
    if x % s:
        answer = False
    return answer