def solution(a, b, n):
    answer = 0
    coke = n
    
    while (coke >= a):
        tmp = coke // a * b # 나눠지는 개수 만큼 더해주기 coke에
        rest = coke % a
        
        coke = tmp
        coke += rest
        
        answer += tmp
        
    return answer