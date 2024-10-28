from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

def bfs(graph, start, target):
    queue = deque([(start, 0)])
    visit = set()

    while queue:
        node, dist = queue.popleft()
        
        if node == target:
            return dist
        
        for neighbor, weight in graph[node]:
            if neighbor not in visit:
                visit.add(neighbor)
                queue.append((neighbor, dist+weight))
    

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for _ in range(m):
    u, v = map(int, input().split())
    print(bfs(graph,u,v))