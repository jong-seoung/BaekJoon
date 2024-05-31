x = int(input())
line = 1
while line < x:
    x -= line
    line += 1
x-=1
if line % 2 == 0:
    res = f'{1+x}/{line-x}'
else:
    res = f'{line-x}/{1+x}'
print(res)