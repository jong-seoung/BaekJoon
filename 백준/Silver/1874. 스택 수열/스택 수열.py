num = int(input())
lst = []
number = []
answer = []
cnt = 0


for i in range(num):
    a = int(input())
    lst.append(a)

for i in range(1,num+1):
    number.append(i)
    answer.append("+")
    while lst[cnt] == number[-1]:
        number.pop(-1)
        answer.append("-")
        cnt += 1
        if len(number) == 0:
            break

if len(number) == 0:
    for i in answer:
        print(i)
else:
    print("NO")