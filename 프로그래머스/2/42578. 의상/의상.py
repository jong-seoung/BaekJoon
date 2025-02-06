from collections import Counter

def solution(clothes):
    ans = []
    for i in clothes:
        ans.append(i[1])
    an = Counter(ans)
    answer = 1
    for i in an.values():
        answer *= (i+1)
    return answer - 1