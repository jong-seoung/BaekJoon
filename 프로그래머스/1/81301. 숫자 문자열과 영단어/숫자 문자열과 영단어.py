def solution(s):
    answer = 0
    num_en = [[0,"zero"],[1,"one"],[2,"two"],[3,"three"],[4,"four"],[5,"five"],[6,"six"],[7,"seven"],[8,"eight"],[9,"nine"]]
    
    for i in num_en:
        s = s.replace(i[1], str(i[0]))
    answer = int(s)
    return answer