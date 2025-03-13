def solution(N, stages):
    answer = []
    res = []
    len_p = len(stages)
    clear_p = 0
    
    for i in range(1, N+1):
        try:
            answer.append((i, stages.count(i) / (len_p - clear_p)))
        except:
            answer.append((i, 0))
        clear_p += stages.count(i)

    answer.sort(reverse=True, key=lambda x: x[1])
    
    for i in answer:
        res.append(i[0])
    return res