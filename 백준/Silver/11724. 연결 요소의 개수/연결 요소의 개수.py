import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


n, m =map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(x):
    visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)