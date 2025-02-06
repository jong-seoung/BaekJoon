def solution(s):
    answer = []
    
    for i in s:
        if i == "(":
            answer.append("(")
        else:
            try:
                pop_item = answer.pop()
                if pop_item != "(":
                    return False
            except:
                return False
    if len(answer) == 0:
        return True
    return False