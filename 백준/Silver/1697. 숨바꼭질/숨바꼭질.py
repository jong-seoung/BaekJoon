from collections import deque


def bfs(start):
    q = deque([start])

    while q:
        n = q.popleft()
        if n == K:
            print(dist[n])
            break
        for i in (n-1, n+1, n*2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[n]+1
                q.append(i)


MAX = 10 ** 5
N, K = map(int, input().split())
dist = [0] * (MAX + 1)

bfs(N)