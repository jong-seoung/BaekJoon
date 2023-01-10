n, k = map(int,input().split())

lst = []

for i in range(n):
    a = int(input())
    lst.append(a)

end = max(lst)
start = 1

while(start <= end):
    mid = (start + end)//2
    cnt = 0
    for i in lst:
        cnt += i // mid
    if cnt >= k:
        start = mid + 1 
    else:
        end = mid - 1

print(end)
    