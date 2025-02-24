def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        sword = 0
        # 루트를 씌운후, 제곱한 값 = 현재 값
        for i in range(1, int(num ** (1/2)) + 1):
            if i*i == num:
                sword += 1
                continue
            if num % i == 0:
                sword += 2
        if sword > limit:
            sword = power
        answer += (sword)
    return answer