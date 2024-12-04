from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    def bfs(start):
        visited[start] = 1
        queue = deque([start])
        
        while queue:
            q = queue.popleft()
            
            for idx, computer in enumerate(computers[q]):
                if computer == 1 and visited[idx] == 0:
                    visited[idx] = 1
                    queue.append(idx)
    
    for i in range(len(computers)):
        if visited[i] == 0:
            bfs(i)
            answer += 1
    return answer