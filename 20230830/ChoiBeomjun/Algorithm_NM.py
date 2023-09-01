def solution(t, p):
    answer = 0
    
    lenP = len(p)
    
    for i in range(0, len(t)):
        if i > len(t) - lenP:
            break
        
        tmp = t[i:i + lenP]
        
        if int(tmp) <= int(p):
            answer += 1
    
    return answer