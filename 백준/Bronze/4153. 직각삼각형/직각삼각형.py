while (1):
    a = list(map(int,input().split()))
    if sum(a) ==0:
        break
    
    b = max(a)
    a.remove(max(a))
    c = []
    for i in a:
        c.append(i**2)
    
    if b**2 == sum(c):
        print("right")
    else:
        print("wrong")
    
