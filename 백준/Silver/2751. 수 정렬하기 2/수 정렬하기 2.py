import sys
n = int(sys.stdin.readline())
b = []

for i in range(n):
    b.append(int(sys.stdin.readline()))

b.sort(reverse=True)

for i in range(n):
    print(b.pop())