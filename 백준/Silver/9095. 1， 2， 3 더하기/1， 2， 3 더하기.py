T = int(input())

for i in range(T):
    n = int(input())
    arr = [0 for i in range(n+3)]
    i = 0
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4

    if n < 4:
        pass
    else:
        for i in range(4, n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
            i += 1
    print(arr[n])
