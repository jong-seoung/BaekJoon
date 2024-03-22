cnt = int(input())
result = 0
if cnt % 4 == 0:
    result = 1
    if cnt % 400 == 0:
        result = 1
    elif cnt % 100 == 0:
        result = 0

print(result)