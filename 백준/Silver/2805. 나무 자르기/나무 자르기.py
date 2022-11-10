import sys
N,M = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(height)


while(start <= end):
    mid = (start+end)//2
    cnt = 0
    for i in height:
        if i > mid:
            cnt += i - mid
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)