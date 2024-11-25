def solution(n, words):
    answer = [0, 0]
    res = [words[0][0]]
    for idx, i in enumerate(words):
        if i[0] != res[-1][-1] or res.count(i) == 1:
            if (idx+1) % n == 0:
                answer = [n, (idx+1)//n]
                break
            else:
                answer = [(idx+1) % n, (idx+1)//n + 1]
                break
        res.append(i)
    
    return answer