def solution(n):
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-1]+lst[i-2])
    return lst[-1] % 1234567

# import sys
# sys.setrecursionlimit(10**7)

# def F(n):
#     if n == 1:
#         return 1
#     return F(n-1) + F(n-2)

# def solution(n):
#     answer = F(n)
#     return answer