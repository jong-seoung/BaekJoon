from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    visited = [0] * (n+1)
    
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    bfs(n, graph, visited)
    answer = visited.count(max(visited))
    return answer

def bfs(n, graph, visited):
    queue = deque([1])
    visited[1] = 1
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == 0:
                visited[i] = visited[q]+1
                queue.append(i)