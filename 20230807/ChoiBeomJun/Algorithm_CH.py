def solution(progresses, speeds):
    answer = []
    
    # 진도가 100%일 때 서비스에 반영 가능 / 뒤가 앞보다 먼저 개발 되었다면 앞이 배포될 때 함께 배포.
    
    
    possibleDays = [] # 배포 가능까지 각 작업당 필요한 일 수
    for index, value in enumerate(progresses):
        day = (100 - value) // speeds[index]
        
        if (100-value) % speeds[index] > 0:
            possibleDays.append(day+1)
        else:
            possibleDays.append(day)
            
    print(possibleDays)

    tmp = possibleDays[0]
    answer.append(1)
    
    # 본격 answer 배열 만들기
    for index, value in enumerate(possibleDays):
        if index > 0 and tmp >= value:
            answer[-1] += 1
        elif index > 0 and tmp < value:
            answer.append(1)
            tmp = value
        
    return answer