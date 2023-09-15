num = int(input())  # 입력받는 숫자
dp = [0, 1]


for i in range(2, num+1):
    min_v = 4
    for j in range(1, int(i**0.5)+1):
        min_v = min(min_v, dp[i-j*j])
    dp.append(min_v+1)
print(dp[num])