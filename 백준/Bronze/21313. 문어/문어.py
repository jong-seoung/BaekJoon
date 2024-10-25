n = int(input())

if n%2 == 0:
    lst = [1,2] *(n//2)
else:
    lst = [1,2] *(n//2)
    lst.append(3)

print(*lst)
