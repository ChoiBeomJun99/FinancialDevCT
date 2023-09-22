# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    x = 0
    answer = []
    box = []
    score.sort(reverse=True)
    for s in score:
        box.append(s)
        if len(box) == m:
            answer.append(box)
            box = []
        
    for a in answer:
        x += min(a) * len(a)
    
    return x