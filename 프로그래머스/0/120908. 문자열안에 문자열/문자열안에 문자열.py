def solution(str1, str2):
    ans = str1.find(str2)
    if ans == -1:
        return 2
    return 1