from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    while len(cities) > 0:
        city = cities.pop(0).upper()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) == cacheSize+1:
                cache.popleft()
    return answer