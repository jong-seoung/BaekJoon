n, m = map(int, input().split())

visited = [False] * 2001
graph = [[] for _ in range(n)]
ans = False

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(index, depth):
    global ans
    visited[index] = True
    if depth == 4:
        ans = True
        return
    for i in graph[index]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth+1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)