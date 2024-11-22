def dfs(answer, x, y, cnt, n, mode):
    answer[x][y]=cnt
    
    if cnt == n * n:
        return
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    nx = dx[mode] + x
    ny = dy[mode] + y

    if not (0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0):
        mode = (mode + 1) % 4  
        nx = x + dx[mode]
        ny = y + dy[mode]

    dfs(answer, nx, ny, cnt + 1, n, mode)
                
def solution(n):
    answer = [[0] * n for _ in range(n)]
    dfs(answer, 0, 0, 1, n, 0)
    
    return answer