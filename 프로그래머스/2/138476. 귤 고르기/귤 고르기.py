import heapq
from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    heap = [-v for v in count.values()]
    heapq.heapify(heap)
    
    answer = 0

    while (k > 0):
        c_tangerine = -heapq.heappop(heap)
        k -= c_tangerine
        answer += 1
    return answer