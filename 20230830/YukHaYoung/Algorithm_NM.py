def solution(t, p):
    answer = 0

    n = len(p)
    
    for i in range(0, len(t)):

        if i+n > len(t):
            continue
        else:
            if int(t[i:i+n]) <= int(p):
                answer += 1
            
    return answer