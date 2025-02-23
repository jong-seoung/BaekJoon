import heapq

def solution(k, score):
    answer = []
    king = []
    heapq.heapify(king)
    
    for i in score:
        heapq.heappush(king, i)
        answer.append(heapq.nlargest(k, king)[-1])
    return answer