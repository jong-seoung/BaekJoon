from collections import Counter

def solution(nums):
    if len(Counter(nums)) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(Counter(nums))
    return answer