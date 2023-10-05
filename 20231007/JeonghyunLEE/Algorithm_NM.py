# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    return_bottle = 0
    rest_bottle = 0
    
    while a <= n:
        return_bottle = (n // a) * b
        rest_bottle = n % a
        answer += return_bottle
        n = rest_bottle + return_bottle
    return answer