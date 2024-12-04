from collections import deque

def solution(begin, target, words):
    answer = 0
    
    def bfs():
        queue = deque([(begin, 0)])
        
        while queue:
            now, step = queue.popleft()
            
            if now == target:
                return step
            
            for word in words:
                count = 0
                for i in range(len(now)):
                    if word[i] != now[i]:
                        count += 1
                
                if count == 1:
                    queue.append([word, step+1])
    if target not in words:
        return answer
    else:
        return bfs()

    return answer