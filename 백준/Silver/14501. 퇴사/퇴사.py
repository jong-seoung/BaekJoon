n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

res = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+graph[i][0],n+1):
        if res[j] < res[i] + graph[i][1]:
            res[j] = res[i] + graph[i][1]

print(res[-1])