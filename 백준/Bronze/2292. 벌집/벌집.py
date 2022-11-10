n = int(input())

cnt = 1
a = 1
while(1):
    if a >= n :
        break
    else:
        a += (6 * cnt)
        cnt += 1
print(cnt)