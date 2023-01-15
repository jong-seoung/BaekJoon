n = int(input())
A = set(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))


for i in num:
    if i in A:
        print(1)
    else:
        print(0)