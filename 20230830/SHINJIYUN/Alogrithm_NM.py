def solution(t, p):
    a = list(t)
    b = list(p)
    x = len(b)
    b_sum = 0
    
    for i in b:
        b_sum = b_sum + i * 10 ^ (x - b[i])
    
    result = 0
        
        
    return result
