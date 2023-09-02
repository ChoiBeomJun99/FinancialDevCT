import itertools

def solution(numbers):
    answer = set()
    comb = list(itertools.combinations(numbers, 2))
    
    for a, b in comb:
        answer.add(a+b)
    
    return sorted(list(answer))