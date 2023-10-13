# Set 을 이용한 풀이
def solution(dirs):
    answer = 0
    rootSet = set()
    x, y = 0, 0 # 현재 좌표 값
    
    for i in dirs: 
        nx, ny = 0, 0
        
        if i == 'U':
            # 위로 1칸
            nx, ny = x, y+1            
        elif i == 'D':
            # 아래로 1칸
            nx, ny = x, y-1
        elif i == 'R':
            # 우측으로 1칸
            nx, ny = x+1, y
        else:
            # 좌측으로 1칸
            nx, ny = x-1, y
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            rootSet.add(((x, y), (nx, ny)))
            rootSet.add(((nx, ny), (x,y)))
            
            # 현재 값 갱신
            x, y = nx, ny
            
        
    return len(rootSet) // 2


# Dict를 이용한 풀이
def solution(dirs):
    answer = 0
    rootDict = dict()
    x, y = 0, 0 # 현재 좌표 값
    
    for i in dirs: 
        nx, ny = 0, 0
        
        if i == 'U':
            # 위로 1칸
            nx, ny = x, y+1            
        elif i == 'D':
            # 아래로 1칸
            nx, ny = x, y-1
        elif i == 'R':
            # 우측으로 1칸
            nx, ny = x+1, y
        else:
            # 좌측으로 1칸
            nx, ny = x-1, y
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if ((x,y), (nx,ny)) not in rootDict:
                rootDict[((x,y), (nx,ny))] = 1
                rootDict[((nx,ny), (x,y))] = 1
            
            # 현재 값 갱신
            x, y = nx, ny
            
        
    return len(rootDict) // 2