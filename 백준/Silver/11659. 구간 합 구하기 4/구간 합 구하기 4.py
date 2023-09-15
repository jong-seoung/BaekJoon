import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 작업 수
score = list(map(int, input().split()))
temp = 0
result = [0]

for i in score:
    temp += i
    result.append(temp)

for i in range(m):
    start, end = map(int, input().split())
    print(result[end]-result[start-1])