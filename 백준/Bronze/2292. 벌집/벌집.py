n = int(input())

start = 1
count = 1
stage = 0

for i in range(1,n):

    if n > start+stage:
        stage += 6 * i
        count += 1

    if n < stage:
        break

print(count)