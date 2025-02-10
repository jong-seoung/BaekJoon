def solution(n, lost, reserve):
    answer = 0
    students = [-1]
    
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for i in range(n):
        students.append(1)
    students.append(-1)
    
    for i in new_lost:
        students[i] -= 1
    
    for i in new_reserve:
        if students[i] == 0:
            students[i] += 1
            
        elif students[i-1] == 0:
            students[i-1] += 1
            
        elif students[i+1] == 0:
            students[i+1] += 1
        print(students)
    print(students)
    return students.count(1)