def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations)):
        h = len(citations) - i
        if h <= citations[i]:
            answer = h
            return answer
    return 0