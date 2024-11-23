def solution(lines):
    lst = []
    answer = 0

    for i in lines:
        for j in range(i[0],i[1]):
            if lst.count(j) == 1:
                answer += 1
            lst.append(j)  
    return answer