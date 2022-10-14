k , n = map(int,input().split())
a = []
for i in range(k):
    a.append(int(input()))

start = 1
long = max(a)

while start <= long:
    mid = (start + long) //2
    line = 0
    for i in a:
        line += i //mid
    
    if line >= n:
        start = mid + 1
    else:
        long = mid -1
print(long)