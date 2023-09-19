from collections import Counter

def solution(topping):
    answer = 0
    topDic = Counter(topping) # 토핑 딕셔너리
    setDic = set() # 비교를 위한 딕셔너리
    
    for i in topping:
        topDic[i] -= 1 # 개수를 하나 빼주고
        setDic.add(i) # 여기서는 더 해준다 (종류의 수만 같으면 되므로)
        
        if topDic[i] == 0: # 0개가 되면 (아예 종류를 삭제)
            topDic.pop(i)
        
        if len(setDic) == len(topDic): # 서로 종류의 수가 같다면 +1 을 해준다.
            answer += 1
    
    return answer