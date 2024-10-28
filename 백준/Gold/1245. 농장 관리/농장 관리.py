import sys
sys.setrecursionlimit(10**6)  # 재귀 한계 설정

n, m = map(int, input().split())  # 격자 크기 입력
graph = [list(map(int, input().split())) for _ in range(n)]  # 높이 정보 입력

# 8방향 이동 정의 (상, 하, 좌, 우 + 대각선)
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# 방문 여부를 추적할 배열
visited = [[False] * m for _ in range(n)]

def dfs(x, y, height):
    visited[x][y] = True  # 현재 칸 방문 처리
    is_peak = True  # 기본적으로 산봉우리라고 가정

    for i in range(8):  # 8방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        # 격자 범위 안에 있을 때만 탐색 진행
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] > height:  # 더 높은 칸이 있다면
                is_peak = False  # 산봉우리 아님
            elif not visited[nx][ny] and graph[nx][ny] == height:
                # 같은 높이인 칸 탐색
                if not dfs(nx, ny, height):
                    is_peak = False  # 재귀 탐색 중 산봉우리 아님이 판별되면 반영

    return is_peak  # 최종적으로 산봉우리 여부 반환

# 산봉우리 개수 세기
count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # 아직 방문하지 않은 칸이면 탐색 시작
            if dfs(i, j, graph[i][j]):  # 이 그룹이 산봉우리라면
                count += 1  # 산봉우리 개수 증가

# 결과 출력
print(count)
