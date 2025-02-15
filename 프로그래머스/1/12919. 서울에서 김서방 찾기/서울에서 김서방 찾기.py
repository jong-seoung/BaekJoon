def solution(seoul):
    answer = ''
    
    for index, i in enumerate(seoul):
        if i=="Kim":
            return f"김서방은 {index}에 있다"
    return answer