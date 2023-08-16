"""
 
*** if (price)^count > money then return==(price)^count-money, else return==0

"""


def solution(price, money, count):
    answer = 0

    for i in range(1, count + 1):
        answer += price * i  # 여기서 반복문 실수... 확인하기~

    if answer > money:
        answer = answer - money
    else:
        answer = 0

    return answer
