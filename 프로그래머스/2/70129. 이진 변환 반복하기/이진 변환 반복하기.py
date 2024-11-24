def solution(s):
    answer = [0, 0]
    while (s != '1'):
        num_1 = s.count('1')
        zero = len(s) - num_1
        answer[1] += zero
        
        s = bin(num_1)[2:]
        answer[0] += 1
    return answer