def solution(s):
    answer = ''
    splitStr = s.split(" ")
    
    for tmp in splitStr:
        for i,v in enumerate(tmp):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        
        answer += " "
    
    answer = answer[0:len(answer)-1]
            
    return answer