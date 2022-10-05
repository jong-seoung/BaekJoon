A = int(input())
B = int(input())
C = int(input())
j = [0,1,2,3,4,5,6,7,8,9]

result =A*B*C
re = list(str(result))

for i in j:
    print(re.count(f"{i}"))
    i+=1
