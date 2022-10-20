import sys
n, k = map(int,sys.stdin.readline().split())
s = 1

for i in range(1,n+1):
    s *= i

for i in range(1,n-k+1):
    s = s // i

for i in range(1,k+1):
    s = s // i

print(s)