import heapq

def solution(n, works):
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    
    for i in range(n):
        r = -heapq.heappop(heap)
        if r == 0:
            break
        heapq.heappush(heap, -(r-1))
    
    answer = 0
    for i in heap:
        answer += i ** 2
    return answer