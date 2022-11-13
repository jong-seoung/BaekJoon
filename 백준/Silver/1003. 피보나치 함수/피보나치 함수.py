import sys

a = int(sys.stdin.readline())

for i in range(a):
    t = int(sys.stdin.readline())
    cnt_result = [1,0,0,1]
    for i in range(t-1):
        cnt_result.append(cnt_result[-2]+cnt_result[-4])
        cnt_result.append(cnt_result[-2]+cnt_result[-4])
    if t == 0:
        print(1,0)
    else:
        print(cnt_result[-2],cnt_result[-1])