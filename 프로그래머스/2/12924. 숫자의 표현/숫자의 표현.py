def solution(n):
    count = 0
    m = 1  # 연속된 수의 개수
    
    while m * (m - 1) // 2 < n:
        # n - (m * (m - 1) / 2)가 m으로 나누어떨어지면 조건 만족
        if (n - (m * (m - 1)) // 2) % m == 0:
            count += 1
        m += 1
    
    return count
