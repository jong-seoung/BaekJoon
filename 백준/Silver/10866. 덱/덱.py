import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push_front":
        lst.insert(0,a[1])
    elif a[0] == "push_back":
        lst.append(a[1])
    elif a[0] == "pop_front":
        if len(lst) <= 0:
            print(-1)
        else:
            print(lst.pop(0))
    elif a[0] == "pop_back":
        if len(lst) <= 0:
            print(-1)
        else:
            print(lst.pop(-1))
    elif a[0] == "size":
        print(len(lst))
    elif a[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0) 
    elif a[0] == "front":
        if len(lst) <= 0:
            print(-1)
        else:
            print(lst[0])
    elif a[0] == "back":
        if len(lst) <= 0:
            print(-1)
        else:
            print(lst[-1])

