a = list(map(int,input().split()))
c= []
for i in a:
    b = i*i
    c.append(b)
print(sum(c)%10)