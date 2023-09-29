def solution(numbers):
    answer = []
    
    def f(x):
        cb = list('0' + bin(x)[2:])
        idx = ''.join(cb).rfind('0')
        cb[idx] = '1'
        
        if x % 2 != 0:
            # 짝수
            cb[idx + 1] = '0'
        
        return int(''.join(cb), 2)
        
        
    for i in numbers:
        answer.append(f(i))
    
    return answer