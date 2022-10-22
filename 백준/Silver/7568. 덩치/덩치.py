import sys
n = int(input())
a = []
for i in range(n):
    x,y = list(map(int,sys.stdin.readline().split()))
    a.append((x,y))


for j in range(n):
    rank = 1
    for i in range(n):
        if a[j][0] < a[i][0] and a[j][1] < a[i][1]:
            rank += 1
    print(rank)