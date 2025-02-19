def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif 97 <= ord(i) <= 122:
            if ord(i) + n > 122:
                i = (ord(i) + n) - 122
                answer += chr(ord('a') + i - 1)
            else:
                answer += chr(ord(i) + n)
        elif 65 <= ord(i) <= 90:
            if ord(i) + n > 90:
                i = (ord(i) + n) - 90
                answer += chr(ord('A') + i - 1)
            else:
                answer += chr(ord(i) + n)
    return answer