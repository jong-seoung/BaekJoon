n = int(input())

fact = 1
for i in range(1,n+1):
    fact = i*fact

fact = list(str(fact))
fact.reverse()

cnt = 0

for i in fact:
    if i == "0":
        cnt += 1
    else:
        print(cnt)
        break