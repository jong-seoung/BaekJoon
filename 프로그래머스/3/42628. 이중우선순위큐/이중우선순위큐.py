import heapq

def solution(operations):
    answer = []
    heap = []
    for i in operations:
        command, num = i.split()
        if command == 'I':
            heapq.heappush(heap, int(num))
            
        elif command == 'D':
            if len(heap) > 0:
                if num == '-1':
                    heapq.heappop(heap)
                else:
                    Max = heapq.nlargest(1,heap)[0]
                    heap.remove(Max)
    if len(heap) > 0:
        answer = [max(heap), heapq.heappop(heap)]
    else:
        answer = [0,0]
    return answer