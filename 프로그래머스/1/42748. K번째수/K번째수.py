def solution(array, commands):
    answer = []
    for i in commands:
        ar = array[i[0]-1:i[1]]
        ar.sort()
        answer.append(ar[i[2]-1])
    return answer