from collections import deque

def solution(order):
    count = 0
    keep = deque([]) # 보조 컨테이너
    
    idx = 1
    while count < len(order):
        # container.popleft()
        
        if order[count] == idx:
            # 그냥 넣는다.
            count += 1
            idx += 1
            
        elif keep and keep[-1] == order[count]:
            # 보조 컨테이너에서 꺼내서 넣는다.
            tmp = keep.pop()
            count += 1
            
        else:
            # 보조 컨테이너에 넣는다.
            keep.append(idx)
            idx += 1
            
        
        # 중단 조건 추가하기
        if keep and order[count] != keep[-1] and idx > len(order) :
            break
        
    
    return count