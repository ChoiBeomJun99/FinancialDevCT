def solution(s):
    answer = ""
    s = s.split(" ")
    for word in s:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    return answer[:-1]
