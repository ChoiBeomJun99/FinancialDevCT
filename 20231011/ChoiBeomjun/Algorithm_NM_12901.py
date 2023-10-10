def solution(a, b):
    day = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}
    
    count = 0
    for i in range(1, a):
        if i == 2:
            # 2월의 경우 (29일)
            count += 29
        elif i % 2 == 0:
            # 짝수 달의 경우 (30일)
            count += 30
        else:
            #홀수 달의 경우 (31일)
            count += 31
            
    # date 더하기
    count += b - 1
    return day[count % 7]
