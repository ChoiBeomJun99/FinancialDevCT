# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    x = len(p)
    for i in range(len(t)-x+1):
        if int(t[i:i+x]) <= int(p):
            answer+=1
    return answer