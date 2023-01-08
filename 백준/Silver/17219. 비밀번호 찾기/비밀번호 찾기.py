n, m = map(int,input().split())

list = {}

for i in range(n):
    key, val = input().split()
    list[key] = val

for i in range(m):
    key = input()
    print(list[key])