T = int(input())
n = int(input())
graph = [[] for i in range(T+1)]
visited = [0 for i in range(T+1)]

for i in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

dfs(1)

print(visited.count(1)-1)