from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(cnt):
    queue = deque([(0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if result[nx][ny] == 0:
                    if graph[nx][ny] <= cnt:
                        result[nx][ny] = -1
                    else:
                        result[nx][ny] = 1
                    queue.append((nx, ny))

def res_bfs(j, k):
    queue = deque([(j, k)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and result[nx][ny] == 1:
                result[nx][ny] = 2
                queue.append((nx, ny))


res = []

for i in range(n):
    res.append(max(graph[i]))
max_dp = max(res)

ans = []

for i in range(max_dp):
    result = [[0]*n for _ in range(n)]
    bfs(i)
    cnt2 = 0
    for j in range(n):
        for k in range(n):
            if result[j][k] == 1:
                res_bfs(j, k)
                cnt2 += 1
    ans.append(cnt2)

print(max(ans))
