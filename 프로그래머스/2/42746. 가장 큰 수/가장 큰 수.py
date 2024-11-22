def solution(numbers):
    lst = []
    for i in numbers:
        lst.append(str(i))
    lst.sort(key=lambda x: x*3, reverse=True)
    answer = ''
    for i in lst:
        answer+=i
    return '0' if answer[0] == '0' else answer
