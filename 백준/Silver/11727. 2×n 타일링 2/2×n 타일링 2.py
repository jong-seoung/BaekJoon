import sys
input = sys.stdin.readline

cnt = int(input())

if cnt < 3:
    result = [0, 1, 3]
else:
    result = [0] * (cnt+1)
    result[1] = 1
    result[2] = 3

if cnt > 2:
    for i in range(3, cnt+1):
        result[i] = result[i-1] + result[i-2] *2
    print(result[cnt] % 10007)
else:
    print(result[cnt])