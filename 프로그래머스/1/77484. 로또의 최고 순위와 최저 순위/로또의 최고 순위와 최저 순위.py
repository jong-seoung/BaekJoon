def solution(lottos, win_nums):
    answer = {0:6, 1:6, 2:5, 3:4 , 4:3, 5:2, 6:1}
    cor = 0 
    
    for i in lottos:
        if i in win_nums:
            cor += 1
    x = lottos.count(0)
    return [answer[cor+x], answer[cor]]