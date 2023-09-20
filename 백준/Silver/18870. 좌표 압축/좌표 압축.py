import sys
input = sys.stdin.readline

test = int(input())
item = list(map(int, input().split()))

item_sort = sorted(set(item))

dic = {item_sort[i]: i for i in range(len(item_sort))}

for i in item:
    print(dic[i], end=' ')
