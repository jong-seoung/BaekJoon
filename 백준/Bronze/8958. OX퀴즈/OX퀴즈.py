test_cnt = int(input())

for i in range(test_cnt):
    result = 0
    cnt = 0
    test_num = list(input())
    for j in test_num:
        if j == "O":
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)
