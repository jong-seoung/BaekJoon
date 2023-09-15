n = int(input())    # 작업 수

for i in range(n):
    cnt = int(input())  # 의상의 수
    name_list = []
    de_name_list = []
    result = 1
    for j in range(cnt):
        name, type = input().split()   # name는 의상 이름, type는 의상 종류
        name_list.append(type)
    de_name_list = list(set(name_list))

    for j in de_name_list:
        result *= name_list.count(j) + 1
    print(result-1)