def solution(numbers):
    res = []
    for i in numbers:
        res.append(str(i))
        
    res.sort(key = lambda x : x*3, reverse=True)
    
    return str(int(''.join(res)))
    