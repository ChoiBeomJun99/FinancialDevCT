def solution(d, budget):
    answer = 0
    d.sort() # 오름차순 정렬
    
    for i in d:
        budget -= i
        
        if budget < 0:
            break
            
        answer += 1
    
    return answer