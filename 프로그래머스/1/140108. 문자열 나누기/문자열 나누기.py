def solution(s):
    answer = 0
    count = 0
    start = s[0]
    
    for idx, i in enumerate(s):
        if i == start:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            answer += 1
            try:
                start = s[idx+1]
            except:
                break
                
    if count != 0:
        answer += 1
        
    return answer