from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for i in range(n+1)]
    
    def bfs(start):
        queue = deque([start])
        visited = [-1] * (n+1)
        visited[start] = 0
        
        while queue:
            q = queue.popleft()
            for i in graph[q]:
                if visited[i] == -1:
                    visited[i] = visited[q] + 1
                    queue.append(i)
        return visited
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
        
    answer = []
    
    distances_from_destination = bfs(destination)
    
    answer = [distances_from_destination[source] for source in sources]
    return answer