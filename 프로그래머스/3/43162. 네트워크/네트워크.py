def dfs(computers, i, visited):
    for num, com in enumerate(computers[i]):
        if visited[num] == 0 and com == 1:
            visited[num] = 1
            dfs(computers, num, visited)


def solution(n, computers):
    visited = [0] * n
    answer = 0
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(computers, i, visited)
            answer+=1 
            
    return answer