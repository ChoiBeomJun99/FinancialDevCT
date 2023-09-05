# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    
    return sorted(list(answer))