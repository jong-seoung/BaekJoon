n = int(input())
grade = list(map(int,input().split()))
max_grade = max(grade)
grade_list=[]

for i in grade:
    g = int(i) / max_grade * 100 
    grade_list.append(g)
print(sum(grade_list)/n)