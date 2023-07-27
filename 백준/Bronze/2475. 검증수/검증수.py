a = map(int, input().split())
cnt = 0

for i in a:
    cnt += i**2
print(cnt % 10)