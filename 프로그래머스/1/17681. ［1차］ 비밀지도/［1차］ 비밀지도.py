def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        num = bin(a1|a2)[2:].zfill(n)
        num = num.replace('1', '#').replace('0', ' ')
        answer.append(num)
    return answer