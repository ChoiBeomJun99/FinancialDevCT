def solution(t, p):
    answer = 0
    t_len, p_len = len(t), len(p)

    for i in range(t_len - p_len + 1):
        num = int(t[i : i + p_len])
        if num <= int(p):
            answer += 1
    return answer
