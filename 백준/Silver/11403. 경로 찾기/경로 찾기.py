from collections import deque


def bfs(start):
    queue = deque([start])
    check = [0 for _ in range(T)]

    while queue:
        n = queue.popleft()

        for i in range(T):
            if g[n][i] == 1 and check[i] == 0:
                queue.append(i)
                check[i] = 1
                visited[start][i] = 1


T = int(input())
g = [list(map(int, input().split())) for i in range(T)]
visited = [[0]*T for i in range(T)]

for i in range(0, T):
    bfs(i)

for i in visited:
    print(*i)