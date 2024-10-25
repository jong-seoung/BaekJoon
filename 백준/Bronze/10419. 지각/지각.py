T=int(input())

for i in range(T):
    d = int(input())
    cnt = 0
    while True:
        if cnt*(cnt+1) < d:
            cnt +=1
        elif cnt*(cnt+1) == d:
            print(cnt)
            break
        else:
            print(cnt-1)
            break