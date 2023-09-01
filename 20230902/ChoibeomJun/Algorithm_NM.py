from itertools import combinations
def solution(numbers):
    answer = []
    tmp = list(combinations(numbers, 2))
    for i in tmp:
        hap = i[0] + i[1]
        if hap not in answer:
            answer.append(hap)
    
    return sorted(answer)