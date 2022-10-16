a = int(input())

for i in range(a):
    h, w, n = map(int,input().split())

    c = 0
    for j in range(n):
        c+=1
        for k in range(1,h+1):
            if c<10:
                k *= 10
            n -= 1
            if n == 0:
                print(f"{k}{c}")
