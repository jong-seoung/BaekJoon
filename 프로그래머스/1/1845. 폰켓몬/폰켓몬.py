def solution(nums):
    answer = 0
    answer = min(len(nums)//2, len(set(nums)))
    return answer