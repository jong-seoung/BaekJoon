cnt = int(input())    # 작업 수


def solution(n):
    for i in range(4, num+1):
        list[i] = list[i-2] + list[i-3]
    print(list[n])


for i in range(cnt):
    num = int(input())
    list = [1] * (num+1)
    if num > 3:
        solution(num)
    else:
        print(1)