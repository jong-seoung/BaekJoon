n, m = map(str, input().split())

def max(n, m):
    N = ''
    M = ''
    for i in n:
        if i == '5':
            i = '6'
        N += i

    for i in m:
        if i == '5':
            i = '6'
        M += i
    return int(N)+int(M)

def min(n, m):
    N = ''
    M = ''
    for i in n:
        if i == '6':
            i = '5'
        N += i

    for i in m:
        if i == '6':
            i = '5'
        M += i
    return int(N)+int(M)

print(min(n, m), max(n,m))