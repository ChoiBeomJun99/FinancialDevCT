def solution(s):
    answer = s
    
    # 영단어를 숫자로 바꿔줄 dictionary 정의
    words = { "zero": 0 , "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    for i in words:
        if i in s:
            # 만약 가지고 있었다면
            answer = answer.replace(i, str(words[i]))
                
    return int(answer)