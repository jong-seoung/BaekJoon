import sys
list = []

n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        list.append(a[1])
    elif a[0] == "pop":
        if len(list) == 0:
            print("-1")
        else:
            print(list.pop(0))
    elif a[0] == "size":
        print(len(list))
    elif a[0] == "empty":
        if len(list) == 0 :
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(list) == 0:
            print("-1")
        else:
            print(list[0])
    elif a[0] == "back":
        if len(list) == 0:
            print("-1")
        else:
            print(list[-1])