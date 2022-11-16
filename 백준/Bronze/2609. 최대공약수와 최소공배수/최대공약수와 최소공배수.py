def a(m,n):
    if n == 0:
        return m
    return a(n,m%n)

m,n = map(int,input().split())

print(a(m,n))
print(m*n//a(m,n))