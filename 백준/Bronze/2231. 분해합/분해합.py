n = int(input())

for i in range(1,n+1):
    a = list(map(int, str(i)))
    b = i + sum(a)
    if b == n:
        print(i)
        break
if b != n :
    print(0)