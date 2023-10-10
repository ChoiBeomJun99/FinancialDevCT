# BFS, DFS 사용하는 문제이다. 
# 'X': 바다, 숫자: 무인도(식량을 나타낸다. - 최대 며칠 머물 수 있는지)
from collections import deque

dx = [0, 0, -1, 1] # 좌, 우 (x좌표)
dy = [1, -1, 0, 0] # 상, 하 (y좌표)

def bfs(maps, i, j, n, m, visited):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1 # 방문했다는 표시이다. 
    area = int(maps[i][j]) # 식량 값.
    
    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 확인하기
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = 1 # 방문 표시
                area += int(maps[nx][ny])
                queue.append((nx, ny))
            
    return area
    

def solution(maps):
    answer = []
    
    # 섬이 존재하지 않으면 -1을 표시한다.
    flag = True
    
    for i in maps:
        if i.count('X') != len(i):
            flag = False
                
    if flag:
        return [-1]
    
    
    # 본격 BFS 시작하기 (queue를 이용한다.)
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0: # 'X'일때는 방문 하지않고 0일때는 아직 방문하지 않은 경우 이므로 방문해야함.
                answer.append(bfs(maps, i, j, n, m, visited))
    
    return sorted(answer)