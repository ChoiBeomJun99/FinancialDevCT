# https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations

def solution(number):
    answer = 0
    
    for n in combinations(number, 3):
        if sum(n) == 0:
            answer += 1
            
    return answer