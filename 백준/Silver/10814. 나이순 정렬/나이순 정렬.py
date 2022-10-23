import sys
n = int(input())
a = []

for i in range(n):
    x,y = list(sys.stdin.readline().split())
    a.append((x,y)) 

a.sort(key = lambda x: int(x[0]))

for i in a:
    print(*i)