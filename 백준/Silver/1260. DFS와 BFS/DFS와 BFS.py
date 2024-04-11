from collections import deque
N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
result = []

for i in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

for i in range(N+1):
    graph[i].sort()


def dfs(n):
    visited[n] = True
    result.append(n)
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(V)
print(*result)
visited = [False for i in range(N+1)]
result = []
bfs(V)
print(*result)
