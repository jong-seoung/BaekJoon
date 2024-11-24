def solution(s):
    cnt = 1
    answer = ''
    for i in s:
        if cnt == 1:
            cnt -= 1
            i = i.upper()
        else:
            i = i.lower()
        if i == ' ':
            cnt += 1
        answer += i
    return answer