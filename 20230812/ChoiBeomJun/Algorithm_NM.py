import math
def solution(n, m):
    answer = []
    
    # ---------- 방법 1 (math 라이브러리 사용) ------------
    
#     # 최대공약수 구하기
#     gcd = math.gcd(n, m)
#     answer.append(math.gcd(n, m))
    
#     # 최소공배수 구하기 **두 수의 곱을 최대공약수로 나누면 최소공배수가 나온다.**
#     answer.append(n * m // gcd)
    
    
    # ---------- 방법 2 (라이브러리 사용 x) ------------
    
    # 최대공약수 구하기
    gcd = m if m > n else n
    while gcd > 1:
        gcd -= 1
        if n % gcd == 0 and m % gcd == 0: # 최대 공약수 발견시
            break
    
    answer.append(gcd)
    
    # 최소공배수 구하기
    answer.append(n * m // gcd)
    
    return answer