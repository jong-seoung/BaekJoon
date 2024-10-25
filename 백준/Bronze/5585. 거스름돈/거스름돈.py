pay = 1000-int(input())

change = [500, 100, 50, 10, 5, 1]
res = 0

for i in change:
    res += pay//i
    pay = pay%i    

print(res)