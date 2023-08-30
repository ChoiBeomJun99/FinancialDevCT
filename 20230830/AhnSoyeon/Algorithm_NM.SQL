def solution(t, p):
    answer = 0
    n = len(p)
    for i in range(len(t)-n+1):
        parts = t[i:i+n]
        if parts <= p:
            answer += 1
    return answer
