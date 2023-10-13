# 더했을때 0이 된다면 삼총사이다. (완전탐색 -> 조합을 이용.)
from itertools import combinations

def solution(number):
    answer = 0
    candidate = combinations(number, 3)
    
    for i in candidate:
        if sum(i) == 0:
            answer += 1
    
    
    return answer