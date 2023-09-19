import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
result = [0] * (N+1)
cnt = 0


def bfs(n):
    result[n] = 1
    for i in graph[n]:
        if result[i] == 0:
            bfs(i)


for i in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(1, N+1):
    if result[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)