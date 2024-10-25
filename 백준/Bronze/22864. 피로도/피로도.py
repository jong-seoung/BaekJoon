A, B, C, M = map(int, input().split())
F = 0
W = 0

for i in range(24):
    if F + A > M:
        F -= C
        if F < 0:
            F = 0
    else:
        F += A
        W += B

print(W)