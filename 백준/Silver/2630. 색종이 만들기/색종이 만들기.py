test = int(input())
graph = [[0]*test for _ in range(test)]

for i in range(test):
    graph[i] = list(map(int, input().split()))

w = 0
b = 0


def make_paper(num, paper):
    global w
    global b
    check = 0

    for i in range(num):
        check += sum(paper[i])

    if check == 0:
        w += 1
    elif check == num * num:
        b += 1
    else:
        temp = [paper[i][0:num//2] for i in range(0, num//2)]
        make_paper(num//2, temp)
        temp = [paper[i][0:num//2] for i in range(num//2, num)]
        make_paper(num//2, temp)
        temp = [paper[i][num//2:num] for i in range(0, num//2)]
        make_paper(num//2, temp)
        temp = [paper[i][num//2:num] for i in range(num//2, num)]
        make_paper(num//2, temp)


make_paper(test, graph)
print(w)
print(b)
