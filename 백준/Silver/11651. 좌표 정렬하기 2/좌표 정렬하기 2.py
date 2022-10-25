import sys
n = int(input())
a = []

for i in range(n):
    x,y = list(map(int,sys.stdin.readline().split()))
    a.append((y,x)) 

a.sort()

for i in a:
    print(i[1],i[0])