n = int(input())

cnt = 1
num2 = 2
num = 1 
if n == 1:
    print(1)
while(n != num):
    for i in range(0,cnt):
        a = num2 * i + 2
        num += 1
        if n == num:
            print(a)
            break
    cnt = cnt * 2
    