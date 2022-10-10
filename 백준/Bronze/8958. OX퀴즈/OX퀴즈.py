a = int(input())

for i in range(a):
    b = str(input().split("X"))
    score = 0
    sum_score = 0
    for j in b:
        if j == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)