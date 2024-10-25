T = int(input())
line = list(map(int, input().split()))
result = [0] * T

for i in range(1,T):
    if line[i-1] > line[i]:
        result[i-1] = 1

print(result.count(0))