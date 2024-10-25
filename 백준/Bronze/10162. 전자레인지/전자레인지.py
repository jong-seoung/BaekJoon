T = int(input())

Time = [300, 60, 10]
Result = []

if T % 10 == 0:
    for i in Time:
        Result.append(T//i)
        T = T%i
    print(*Result)
else:
    print(-1)
