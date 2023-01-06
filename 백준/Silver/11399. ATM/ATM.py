num = int(input())

total = 0

time = list(map(int,input().split()))

time.sort()

for i in range(num):
    for j in range(num-i):
        total += time[j]
        
print(total)