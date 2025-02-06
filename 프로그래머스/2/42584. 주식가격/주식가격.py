
# def solution(prices):
#     answer = []
    
#     while len(prices) > 0:
#         curr = prices.pop(0)
#         count = 0
#         for i in prices:
#             count+=1
#             if curr > i:
#                 break
#         answer.append(count)
#     return answer

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        curr = queue.popleft()
        count = 0
        for i in queue:
            count+=1
            if curr > i:
                break
        answer.append(count)
    return answer