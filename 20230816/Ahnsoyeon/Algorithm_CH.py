from collections import deque

def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    rtime = 0
    for city in cities:
        city = city.lower()
        if city not in dq: # cache miss
            dq.append(city)
            rtime += 5
        else: # cache hit
            dq.remove(city)
            dq.append(city)
            rtime += 1

    return rtime
