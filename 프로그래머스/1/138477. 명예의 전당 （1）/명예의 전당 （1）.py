import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for i in score:
        heapq.heappush(heap, i)
        king = heapq.nlargest(k, heap)
        answer.append(king[-1])
    return answer