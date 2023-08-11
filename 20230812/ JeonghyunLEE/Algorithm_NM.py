# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
        
    for j in range(max(n,m), m*n+1):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
        
    return answer