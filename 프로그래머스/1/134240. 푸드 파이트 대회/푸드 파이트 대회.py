def solution(food):
    answer = ''
    cnt = 0
    for i in food:
        if i > 0 and i % 2 == 1:
            i -= 1
        answer = answer[0:len(answer)//2] + str(cnt)*i + answer[len(answer)//2:]
        cnt += 1
    answer = answer[0:len(answer)//2] + '0' + answer[len(answer)//2:]
    return answer