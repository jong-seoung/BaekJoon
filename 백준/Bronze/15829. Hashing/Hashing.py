n = int(input())
a = input()
b = []
c= []
d=0
for i in a:
    c.append(i)
for i in c:
    if i == "a":
        b.append(1)
    elif i =="b":
        b.append(2)
    elif i =="c":
        b.append(3)
    elif i =="d":
        b.append(4)
    elif i =="e":
        b.append(5)
    elif i =="f":
        b.append(6)
    elif i =="g":
        b.append(7)
    elif i =="h":
        b.append(8)
    elif i =="i":
        b.append(9)
    elif i =="j":
        b.append(10)
    elif i =="k":
        b.append(11)
    elif i =="l":
        b.append(12)
    elif i =="m":
        b.append(13)
    elif i =="n":
        b.append(14)
    elif i =="o":
        b.append(15)
    elif i =="p":
        b.append(16)
    elif i =="q":
        b.append(17)
    elif i =="r":
        b.append(18)
    elif i =="s":
        b.append(19)
    elif i =="t":
        b.append(20)
    elif i =="u":
        b.append(21)
    elif i =="v":
        b.append(22)
    elif i =="w":
        b.append(23)
    elif i =="x":
        b.append(24)
    elif i =="y":
        b.append(25)
    elif i =="z":
        b.append(26)

for i in range(n):
    d+=b[i]*(31**i)
    

print(d%1234567891)