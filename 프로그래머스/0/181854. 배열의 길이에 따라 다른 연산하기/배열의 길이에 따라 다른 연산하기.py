def solution(arr, n):
    answer = []
    l = len(arr)
    
    start = 0
    
    if l % 2 == 0:
        start = 1
    
    while(start<=l):
        arr[start] = arr[start] + n
        start += 2
        
    answer = arr

    return answer