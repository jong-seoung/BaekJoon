n = int(input())

for i in range(n):
    a,b = input().split()
    c = ''
    for j in list(b):
        c += j * int(a)
    print(c)