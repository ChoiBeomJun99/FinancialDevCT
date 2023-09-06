def solution(s, n):
    result = []
    
    for char in s:
        if char.isalpha():  # 알파벳인 경우만 밀어서 변환
            start = ord('a') if char.islower() else ord('A')
            changeAlpha = chr((ord(char) - start + n) % 26 + start)
        else:
            changeAlpha = char  # 공백 및 다른 문자는 그대로
        
        result.append(changeAlpha)

    return ''.join(result)