n,m = map(int,input().split())
card = list(map(int,input().split()))

lst = []

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = card[i]+card[j]+card[k]
            if sum <= m:
                lst.append(sum)

print(max(lst))
