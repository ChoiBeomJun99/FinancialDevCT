# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque
def solution(cacheSize, cities):
    
    # 캐시사이즈가 0일 때
    if cacheSize == 0:
        return len(cities) * 5
    
    # 대소문자 구분 X
    upper_cities = []
    for c in cities:
        upper_cities.append(c.upper())
    
    cache = deque()
    time = 0
    
    for uc in upper_cities:
        # 캐시에 있을 때
        if uc in cache:
            cache.remove(uc)
            cache.append(uc)
            time += 1
        # 캐시에 없을 때
        else:
            # 캐시가 다 찼을 때
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(uc)
            time += 5
    
    return time