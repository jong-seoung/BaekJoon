line = int(input())
f_star = "*"
star = "*"
space =" "

while line > 0:
    print(space*(line-1)+star)
    star += f_star
    line -= 1 
