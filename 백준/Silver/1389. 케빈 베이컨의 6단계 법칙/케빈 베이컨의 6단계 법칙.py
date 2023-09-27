from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
result = []


def bfs(graph, start):
    num = [0] * (N+1)
    queue = deque()
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if i not in visited:
                num[i] = num[n] + 1
                queue.append(i)
                visited.add(i)
    return sum(num)


for i in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


for i in range(1, N+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1)
