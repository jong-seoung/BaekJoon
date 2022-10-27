n,k = map(int,input().split())
a = [i for i in range(1,n+1)]
b = []

for h in range(n):
    for i in range(k-1):
        a.append(a.pop(0))
    b.append(str(a.pop(0)))
print("<", ", ".join(b), ">", sep="")