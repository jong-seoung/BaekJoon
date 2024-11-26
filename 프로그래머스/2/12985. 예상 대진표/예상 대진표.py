import math

def solution(n, a, b):
    round_count = 0  # 현재 라운드

    # A와 B가 같은 번호가 될 때까지 반복
    while a != b:
        # 다음 라운드 번호 계산
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        round_count += 1

    return round_count
