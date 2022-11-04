a,b = input().split()
lst = []
lst.append(a[::-1])
lst.append(b[::-1])
print(max(lst))