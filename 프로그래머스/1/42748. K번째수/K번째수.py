def solution(array, commands):
    answer = []
    for i in commands:
        arr2 = array[i[0]-1:i[1]]
        arr2.sort()
        answer.append(arr2[i[2]-1])
    return answer