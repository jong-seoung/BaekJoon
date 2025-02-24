def solution(name, yearning, photo):
    answer = []
    score = {}
    for n, y in zip(name, yearning):
        score[n] = y
    
    for i in photo:
        t_score = 0
        for j in i:
            if j in score:
                t_score+=score[j]
        answer.append(t_score)
    return answer