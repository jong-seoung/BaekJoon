import sys
from collections import Counter
n = sys.stdin.readline()
c = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
d = list(map(int,sys.stdin.readline().split()))
a = []

count= Counter(c)

for i in d:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')