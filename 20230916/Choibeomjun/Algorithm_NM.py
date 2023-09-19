def solution(food):
    answer = ''
    
    for i, v in enumerate(food):
        if i > 0:
            for j in range(0, v//2):
                answer += str(i)
    
    tmp = list(answer)
    tmp.reverse()
    return answer + '0' + ''.join(tmp)