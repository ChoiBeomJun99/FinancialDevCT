def solution(strings, n):
    answer = []
    strings.sort()

    strings = sorted(strings, key = lambda x: x[n])

    return strings