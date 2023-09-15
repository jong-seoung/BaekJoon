import sys
input = sys.stdin.readline

cnt = int(input())
result = [0, 1, 2] * (cnt + 1)
if cnt > 2:
    for i in range(3, cnt+1):
        result[i] = result[i-1] + result[i-2]
    print(result[cnt] % 10007)
else:
    print(result[cnt])