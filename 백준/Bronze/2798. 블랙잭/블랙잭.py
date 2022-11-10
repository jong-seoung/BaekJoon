N,M = map(int,input().split())
card = list(map(int,input().split())) 
lst = []
lst2 = []

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            cnt = card[i]+card[j]+card[k]
            if M - cnt >= 0:
                lst.append(cnt)
 
print(max(lst))