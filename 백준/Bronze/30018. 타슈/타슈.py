N = int(input())

origin = list(map(int, input().split()))
last = list(map(int, input().split()))

res = 0
for i in range(N):
    res += abs(origin[i]-last[i])

print(res//2)