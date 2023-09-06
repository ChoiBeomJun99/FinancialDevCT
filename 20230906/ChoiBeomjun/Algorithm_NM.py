def solution(s, n):
    answer = ''
    
    for i in s:
        asciiNum = ord(i) + n
        
        # 대문자 소문자 구분 해야함
        if i.islower():
            # 소문자
            if asciiNum > ord("z"):
                answer += chr(ord("a") + asciiNum - ord("z") -1)
            else:
                answer += chr(asciiNum)
                
        elif i.isupper():
            # 대문자
            if asciiNum > ord("Z"):
                answer += chr(ord("A") + asciiNum - ord("Z") -1)
            else:
                answer += chr(asciiNum)
        
        else:
            answer += i
            

    return answer