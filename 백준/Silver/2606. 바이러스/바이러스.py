n = int(input())    # 컴퓨터 수
v = int(input())    # 연결선 수
graph = [[] for i in range(n+1)]    # 그래프 생성
visited = [0] * (n+1)   # 방문 여부

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a] # 양방향 연결

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)