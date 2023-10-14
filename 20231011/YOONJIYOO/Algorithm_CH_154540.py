# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# resursionlimit을 지정하지 않으면 오류가 뜨므로 주의


import sys
sys.setrecursionlimit(10**6)

def dfs(a,b,graph,visited,cnt):

    visited[a][b]=True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):

        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<len(visited) and 0<=ny<len(visited[0]):
            if not visited[nx][ny] and graph[nx][ny] != 'X':
                cnt[0]+=int(graph[nx][ny])
                dfs(nx,ny,graph,visited,cnt)



def solution(maps):
    answer = []
    graph = []

    for i in maps:
        elem = list(i)
        graph.append(elem)

    N = len(graph)
    M = len(graph[0])
    visited = [ [ 0 for _ in range(M) ] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] != 'X':
                cnt = []
                cnt.append(int(graph[i][j]))
                dfs(i,j,graph,visited,cnt)
                answer.append(cnt[0])

    answer.sort()
    if not answer:
        answer.append(-1)
    return answer