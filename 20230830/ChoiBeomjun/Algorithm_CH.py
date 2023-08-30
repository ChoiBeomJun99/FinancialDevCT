def solution(want, number, discount):
    answer = 0
    wantWithNumber = [] # 원하는 품목 * 그에 해당하는 개수 곱하기를 반영한 리스트
    
    for i, v in enumerate(number):
        for j in range(0, v):
            wantWithNumber.append(want[i])
    
    day = len(wantWithNumber)
    for i, v in enumerate(discount):
        # 매 회수 비교할 임의 변수에 저장
        tmp = [i for i in wantWithNumber]
        
        # 종료 조건
        if i > len(discount) - day:
            break
        
        # 본격 비교 리스트에서 비교 / 제거 실시
        for j in range(i, i + day):
            if discount[j] in tmp:
                tmp.remove(discount[j])
        
        # 만약 제거가 모두 되었다면 이는 +1을 해준다.
        if len(tmp) == 0:
            answer += 1
        
        
    return answer