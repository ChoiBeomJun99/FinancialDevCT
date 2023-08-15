def solution(cacheSize, cities):
    # LRU 알고리즘 구현 문제 - 가장 오래된 페이지를 교체한다. hit +1 / miss +5    
    executionTime = 0 # 총 실행 시간 (return 값)
    
    nowCache = [] # 현재 캐시에 들어가 있는 리스트
    nowCacheOrder = [] # 현재 캐시에 들어가 있는 도시들의 들어간 시간
    
    # 캐시사이즈 0인 경우 예외처리
    if cacheSize == 0: 
        return 5 * len(cities)
    
    order = 0 # 자신이 캐시에 들어간게 몇번째인지
    # 실행할 도시 이름 리스트가 빌 때까지 실행
    while len(cities) > 0:
        tmp = cities.pop(0)
        tmp = tmp.upper() # 대소문자 구분 없으므로 다 대문자로 변경
        
        if tmp in nowCache:
            # hit (1번의 경우)
            idx = nowCache.index(tmp)
            nowCacheOrder[idx] = order # order 업데이트 (가장 최근 사용)
            executionTime += 1
        else:
            # miss
            executionTime += 5
            
            if len(nowCache) < cacheSize:
                nowCache.append(tmp)
                nowCacheOrder.append(order)    
            else:
                # miss (LRU 알고리즘 발동해야함)
                minOrder = min(nowCacheOrder) # 가장 오래된 지역 찾기
                idx = nowCacheOrder.index(minOrder) # 지워야할 idx 찾기

                # 지우기
                nowCache.pop(idx)
                nowCacheOrder.pop(idx)

                # 페이징 작업
                nowCache.append(tmp)
                nowCacheOrder.append(order)
            
        # 순서 표기            
        order += 1
    
    return executionTime