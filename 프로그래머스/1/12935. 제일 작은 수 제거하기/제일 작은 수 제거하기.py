def solution(arr):
    arr.remove(min(arr))
    
    if not len(arr):
        arr = [-1]
    return arr