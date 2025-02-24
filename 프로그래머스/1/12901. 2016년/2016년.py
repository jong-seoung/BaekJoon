import datetime

def solution(a, b):
    weeks = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    answer = weeks[(datetime.datetime(2016, a, b)).weekday()]
    return answer