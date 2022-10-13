n = int(input())
a = []
count = 0
nu = 0

while(1):
    nu += 1
    for i in str(nu):
        if (i == "6"):
            count += 1
            if count == 3:
                a.append(nu)   
        else:
            count = 0
    count = 0
    if len(a) == n:
        break
print(nu)