def solution(price, money, count):
    total = 0
    
    for n in range(1, count+1):
        total += price * n
        
    if total-money <= 0:
        return 0
    
    return total - money