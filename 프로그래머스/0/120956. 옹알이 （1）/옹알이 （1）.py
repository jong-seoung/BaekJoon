def solution(babbling):
    lst = ['aya','ye','woo','ma']
    answer = 0
    for i in babbling:
        for j in lst:
            i = i.replace(j,'1')
        i = i.replace('1','')
        if i == '':
            answer+=1
    return answer