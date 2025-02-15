def solution(s):
    answer = True
    s = s.lower()
    print(s, s.count('y'), s.count('p'))
    if s.count('y') != s.count('p'):
        answer = False
    return answer