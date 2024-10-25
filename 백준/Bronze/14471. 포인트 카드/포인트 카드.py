n, m = map(int, input().split())
lst = []
cnt = 0
res = 0

for _ in range(m):
    a, b = map(int, input().split())
    if a >= n:
        cnt += 1
    else:
        lst.append(n-a)

lst.sort()

for i in range(m-1-cnt):
    res += lst[i]

print(res)