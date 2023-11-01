N = int(input())
graph = [list(map(int, input())) for i in range(N)]


def dfs(x, y):
        dx = [0, 0, 0, -1, 1]
        dy = [0, -1, 1, 0, 0]

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    result[cnt-1] += 1
                    dfs(nx, ny)

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if graph[j][i] == 1:
            cnt += 1
            result.append(0)
            dfs(i, j)

print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])
