def solution(s):
    answer = s.split(' ')
    result = ''
    for i in answer:
        for idx, j in enumerate(i):
            if idx % 2 == 1:
                j = j.lower()
            else:
                j = j.upper()
            result += j
        result += ' '
    return result[:-1]