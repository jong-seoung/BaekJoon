t = int(input())
for i in range(t):
    sum, R = input().split()
    s = ""
    for i in R:
         s += int(sum) * i
    print(s)    