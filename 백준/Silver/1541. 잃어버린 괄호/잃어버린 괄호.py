text = list(input().split("-"))
result_list = []

for i in text:
    cnt = 0
    temp = i.split("+")
    for j in temp:
        cnt += int(j)
    result_list.append(cnt)

result = result_list[0]
for i in result_list[1:]:
    result -= i
print(result)