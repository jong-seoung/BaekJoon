N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
res = []

def dfs(x, y):
    graph[x][y]=0
    res[cnt-1] += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            res.append(0)
            dfs(i, j)

print(cnt)

res.sort()
for i in res:
    print(i)