n = int(input())
s = [int(input()) for i in range(n)]
d = [0] * (n)

if len(s) < 2:
    print(sum(s))
else:
    d[0] = s[0]
    d[1] = s[0] + s[1]
    for i in range(2,n):
        d[i] = max(d[i-3]+s[i-1]+s[i], d[i-2]+s[i])
    print(d[-1])