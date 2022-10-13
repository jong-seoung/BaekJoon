n = int(input())
b = []

for i in range(n):
    b.append(input())

c = list(set(b))
c.sort()
c.sort(key=len)

for i in c:
    print(i)