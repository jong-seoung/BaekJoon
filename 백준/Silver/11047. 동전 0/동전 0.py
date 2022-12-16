n, k = map(int,input().split())

num = []

for i in range(n):
    num.append(int(input()))

cnt = 0
for i in range(n):
    cnt += k // num[n-1]
    k = k % num[n-1]
    n -= 1


print(cnt)