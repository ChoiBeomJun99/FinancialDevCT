from itertools import combinations
def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(answer)
