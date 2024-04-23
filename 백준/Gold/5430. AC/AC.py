import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    lst = list(map(str, input().rstrip()[1:-1:].split(',')))
    queue = deque(lst)
    flag, rcnt, front, back = 0, 0, 0, len(queue) -1

    if n == 0:
        queue = []
        front = 0
        back = 0

    for i in p:
        if i == 'R':
            rcnt += 1
        elif i == 'D':
            if len(queue) < 1:
                flag = 1
                print('error')
                break
            else:
                if rcnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
         
    if flag == 0:
        if rcnt % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
