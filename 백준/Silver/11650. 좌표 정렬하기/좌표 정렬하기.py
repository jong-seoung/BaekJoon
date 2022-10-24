import sys
n = int(input())
a = []

for i in range(n):
    x,y = list(map(int,sys.stdin.readline().split()))
    a.append((x,y)) 

a.sort()

for i in a:
    print(*i)