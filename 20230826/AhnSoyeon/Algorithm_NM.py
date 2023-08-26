from itertools import combinations #itertools내 combinations함수를 사용하겠다.
def solution(number):
    return list(map(sum,list(combinations(number,3)))).count(0)
