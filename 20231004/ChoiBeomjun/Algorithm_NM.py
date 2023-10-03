def solution(dartResult):
    answer = 0
    renewl = [] # split한 결과를 따로 담는 과정
    
    # renewl 리스트 만들기
    lastDigit = 0
    for i, v in enumerate(dartResult):
        if i > 0 and v.isdigit() and not dartResult[i-1].isdigit():
            renewl.append(dartResult[lastDigit: i])
            lastDigit = i
    
    renewl.append(dartResult[lastDigit:])
    
    score = []
    scoreIdx = -1
    for i in renewl:
        idx = 1 if i[1] == '0' else 0            
        nowScore = 10 if idx == 1 else int(i[idx]) # 현재 점수        
        
        if i[idx + 1] == 'D':
            nowScore = nowScore ** 2
        elif i[idx + 1] == 'T':
            nowScore = nowScore ** 3
            
        # 옵션 여부 체크 
        if idx == 0 and len(i) == 3 or idx == 1 and len(i) == 4:
            if i[idx + 2] == '#':
                # 아차상
                nowScore *= -1
            elif i[idx + 2] == '*':
                # 스타상
                nowScore = nowScore * 2
                if scoreIdx > -1:
                    score[scoreIdx] *= 2
        
        score.append(nowScore)
        scoreIdx += 1
        
    return sum(score)