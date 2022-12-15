import sys

a ,b = map(int,sys.stdin.readline().split())

aset = set()
for i in range(a):
    aset.add(input())

bset = set()
for i in range(b):
    bset.add(input())

re = sorted(list(aset & bset))
print(len(re))
for i in re:
    print(i)