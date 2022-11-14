import sys

n = int(sys.stdin.readline())
s = []
for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == "add":
        if s.count(a[1])==1:
            pass
        else:
            s.append(a[1])
    elif a[0] == "remove":
        if s.count(a[1]) == 0:
            pass
        else:
            s.remove(a[1])
    elif a[0] == "check":
        if s.count(a[1]) == 1:
            print(1)
        else:
            print(0)
    elif a[0] == "toggle":
        if s.count(a[1]) == 0:
            s.append(a[1])
        else:
            s.remove(a[1])
    elif a[0] =="all":
        s=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    elif a[0] == "empty":
        s = []