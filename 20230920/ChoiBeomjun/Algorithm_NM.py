# k = max(m)
# m = 사과를 m개씩 담는다.
# score = 사과들의 점수, len(score) = 사과들의 개수
def solution(k, m, score):
    answer = 0
            
    score = sorted(score, reverse=True)
    for i in range(0, len(score), m):
        if i+m > len(score):
            break
        
        tmp = score[i:i+m]
        answer += (min(tmp) * m)
        
    return answer