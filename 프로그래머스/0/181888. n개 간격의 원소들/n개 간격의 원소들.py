def solution(num_list, n):
    answer = []
    for num in num_list[0::n]:
        answer.append(num)
    return answer