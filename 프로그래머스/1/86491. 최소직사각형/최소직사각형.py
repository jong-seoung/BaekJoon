def solution(sizes):
    x = []
    y = []
    for i in sizes:
        i.sort()
        x.append(i[0])
        y.append(i[1])
    answer = max(x) * max(y)
    return answer