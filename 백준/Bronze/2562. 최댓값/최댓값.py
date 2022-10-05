nu = []

for i in range(9):
    nu.append(int(input()))

print(max(nu))
print(nu.index(max(nu))+1)