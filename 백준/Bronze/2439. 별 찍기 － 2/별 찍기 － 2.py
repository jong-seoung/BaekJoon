l = int(input())
s = "*"
b = " "

for i in range(1,l+1):
    print("{0}{1}".format(b*(l-i),s*i))
