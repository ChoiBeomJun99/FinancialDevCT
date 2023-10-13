# https://school.programmers.co.kr/learn/courses/30/lessons/49994

from collections import defaultdict

def solution(dirs):
    answer = []
    now_x, now_y = 0,0
    dx = [0, 0, 1, -1] # U D R L
    dy = [1, -1, 0, 0]
    path_count = defaultdict(int)
    
    for d in dirs:
        if d == 'U' and now_y < 5:
            now_x += dx[0]
            now_y += dy[0]
        elif d == 'D' and now_y > -5:
            now_x += dx[1]
            now_y += dy[1]
        elif d == 'R' and now_x < 5:
            now_x += dx[2]
            now_y += dy[2]
        elif d == 'L' and now_x > -5:
            now_x += dx[3]
            now_y += dy[3]
        answer.append([now_x, now_y])
    print(answer)
    for a in answer:
        path_count[str(a)] += 1
    print(path_count)
    
    return len(path_count)