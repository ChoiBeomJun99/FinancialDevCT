# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    rev = ''
    
    for i, f in enumerate(food):
        x = int(f / 2)
        if x:
            answer += str(i) * x
    
    for a in sorted(list(answer), reverse = True):
        rev += str(a)
        
    return answer + '0' + rev