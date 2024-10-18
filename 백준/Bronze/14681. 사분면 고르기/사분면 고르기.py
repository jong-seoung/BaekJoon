X = int(input())
Y = int(input())

cnt = 1

if X <= 0:
    if Y <= 0:
        print(3)
    else:
        print(2)
else:
    if Y <= 0:
        print(4)
    else:
        print(1)