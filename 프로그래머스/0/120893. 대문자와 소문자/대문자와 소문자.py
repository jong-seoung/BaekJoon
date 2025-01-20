def solution(my_string):
    answer = ''
    for string in my_string:
        if ord(string) > 90:
            answer += string.upper()
        else:
            answer += string.lower()
    return answer