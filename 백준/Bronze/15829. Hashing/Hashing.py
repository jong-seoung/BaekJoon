n = int(input())
a = input()
b = [] 
d=0

for i in a:
    b.append(ord(i)-96)

for i in range(n):
    d+=b[i]*(31**i)
    

print(d%1234567891)
        