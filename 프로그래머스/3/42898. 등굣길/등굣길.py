def solution(m, n, puddles):
    graph = [[0] * m for i in range(n)]
    for puddle in puddles:
        graph[puddle[1]-1][puddle[0]-1] = -1    
        
    graph[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:
                graph[i][j] = 0
            else:
                if i > 0:
                    graph[i][j] += graph[i-1][j]
                if j > 0:
                    graph[i][j] += graph[i][j-1]
    return graph[-1][-1] % 1000000007