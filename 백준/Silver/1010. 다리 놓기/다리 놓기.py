import sys

input = sys.stdin.readline

def factoryer(index):
    return index * factoryer(index-1) if index > 1 else 1

t = int(input())

for i in range(t):
    m, n = map(int, input().split())    
    print(factoryer(n) // (factoryer(m) * factoryer(n-m)))

