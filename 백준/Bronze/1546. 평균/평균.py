n = int(input())
a = list(map(int,input().split()))
b = []
m = max(a)

for i in a:
    A = i/m*100
    b.append(A)

print(sum(b)/len(b))