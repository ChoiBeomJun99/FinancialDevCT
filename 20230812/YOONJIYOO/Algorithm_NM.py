def solution(n, m):
    answer = []
    a, b = n, m
    while True:  # 최대공약수 구하기
        if b == 0:  # 최대공약수 찾은 경우
            answer.append(a)
            answer.append(n * m // a)  # 최소공배수
            break
        else:
            a, b = b, a % b  # Swap
    return answer
