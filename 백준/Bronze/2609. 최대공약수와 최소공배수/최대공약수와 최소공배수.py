def gcd(m, n):
    if n == 0:
        return m
    return gcd(n,m%n)
    
m, n = map(int, input().split())

print(gcd(m, n))
print(m*n//gcd(m, n))