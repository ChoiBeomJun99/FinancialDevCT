# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    score = set(i for i in range(11))
    area = {'S' : 1, 'D': 2, 'T' : 3}
    new = []
    cnt = 0
    num = 0

    for s in dartResult:
        if s in str(score):
            if num != 0:
                num = (int(str(num) + s))
                continue
            num = int(s)
        else:
            if s == "S":
                new.append(pow(num, area[s]))
                cnt += 1
            elif s == "D":
                new.append(pow(num, area[s]))
                cnt += 1
            elif s == "T":
                new.append(pow(num, area[s]))
                cnt += 1
            elif s == "*":
                if cnt == 1:
                    new[-1] = new[-1] * 2
                else:
                    new[-1], new[-2] = (new[-1] * 2), (new[-2] * 2)
            elif s == "#":
                new[-1] = -new[-1]
            num = 0

    answer = sum(new)

    return answer