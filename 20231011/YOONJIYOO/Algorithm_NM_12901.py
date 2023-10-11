# https://school.programmers.co.kr/learn/courses/30/lessons/12901


def solution(a, b):
    answer = ""
    days = 0
    year = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]  # 금요일부터 시작

    for i in range(1, a):
        days += year[i]
    days += b

    return day[days % 7 - 1]
