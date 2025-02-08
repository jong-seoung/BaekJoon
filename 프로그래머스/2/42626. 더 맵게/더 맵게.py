import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        try:
            hp1 = heapq.heappop(scoville)
            hp2 = heapq.heappop(scoville)
            heapq.heappush(scoville, hp1 + (hp2*2))
            answer += 1
        except:
            return -1

    return answer