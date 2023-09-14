n = int(input())    # 작업 수

for i in range(n):

    num = int(input())
    d = [0] * (num + 2)
    re = 4
    if num == 1:
        d[1] = 1
    elif num == 2:
        d[2] = 2
    elif num == 3:
        d[3] = 4
    else:
        d[1] = 1
        d[2] = 2
        d[3] = 4
        while(re < num+1):
            d[re] = d[re-1] + d[re-2] + d[re-3]
            re += 1
    print(d[num])