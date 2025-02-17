def solution(price, money, count):
    answer = [price]
    for i in range(count-1):
        answer.append(answer[-1]+price)
    
    if sum(answer) - money > 0:
        return sum(answer) - money
    else:
        return 0
