import math
test_cnt = int(input())

for i in range(test_cnt):
    h, w, n = map(int, input().split())
    cnt = 0

    for j in range(1, w+1):
        for k in range(1, h+1):
            cnt += 1
            if cnt == n:
                if j < 10:
                    print(f"{k}0{j}")
                else:
                    print(f"{k}{j}")
                break


