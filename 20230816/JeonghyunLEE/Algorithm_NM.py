# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    tot = 0
    for c in range(1, count+1):
        tot += price * c
    
    if money - tot <= 0:
        return money - tot
    else:
        return 0