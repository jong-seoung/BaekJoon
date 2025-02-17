import heapq

def solution(d, budget):
    ans = 0
    answer = 0
    heapq.heapify(d)
    
    while d:
        price = heapq.heappop(d)
        if answer + price <= budget:
            answer += price
            ans += 1
        else:
            break
    return ans