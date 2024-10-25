n = int(input())

cnt = 0
res = 0

for i in list(map(int, input().split())):
    if i == cnt:
        cnt+=1
        res+=1
    if cnt == 3:
        cnt = 0

print(res)