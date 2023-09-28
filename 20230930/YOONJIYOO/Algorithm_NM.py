def solution(d, budget):
    answer = 0
    d.sort()

    while budget < sum(d):
        d.pop()
    return len(d)
