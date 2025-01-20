import math
def solution(n):
    rot = math.ceil(n ** (1/2))
    if n == rot ** 2:
        return 1
    return 2