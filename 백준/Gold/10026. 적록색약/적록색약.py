import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]

def dfs(x,y):
    visited[x][y] = 1
    col = graph[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] == col:
                dfs(nx, ny)

for i in range(n):
    graph.append(list(map(str, input())))

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i,j)

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

ncnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            ncnt += 1
            dfs(i,j)

print(cnt)
print(ncnt)