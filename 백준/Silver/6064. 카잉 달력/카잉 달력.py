def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


T = int(input())

for i in range(T):
    m, n, x, y = map(int, input().split())
    year = [1, 1]
    print(num(m, n, x, y))