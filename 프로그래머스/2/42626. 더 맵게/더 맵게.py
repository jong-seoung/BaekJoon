import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        Min = heapq.heappop(scoville)
        Next = heapq.heappop(scoville)
        new_scoville = Min + Next*2
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
        
    return -1 if scoville[0] < K else answer