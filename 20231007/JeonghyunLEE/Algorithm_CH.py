# https://school.programmers.co.kr/learn/courses/30/lessons/17683#

# 테스트케이스 27 실패.. 왜지,,?
# 조건 일치할 때
# 1. 재생시간이 제일 긴 것
# 2. 재생시간 같을 때, 먼저 입력된 음악 제목

def m_time(m):
    return 60 * abs(int(m[0].split(":")[0]) - int(m[1].split(":")[0])) + abs(int(m[0].split(":")[1]) - int(m[1].split(":")[1]))

def sub_sharp(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = []
    cnt = 0
    song = dict()
    m = sub_sharp(m)
    
    for i in range(len(musicinfos)):
        x = musicinfos[i].split(",")
        # musicinfos안의 #코드 대치
        x[3] = sub_sharp(x[3])
        #재생된 시간
        if m_time(x) > len(x[3]): # 길 때
            song[(x[3] * (m_time(x) // len(x[3])) + x[3][:m_time(x)%len(x[3])])] = [x[2], m_time(x)]
        else: # 짧거나 같을 때
            song[x[3][:m_time(x)]] = [x[2], m_time(x)]
    
    # 음악이 키 안에 존재할 때, [음악명, 재생시간, cnt(입력순서)]
    for s in song.keys():
        if m in s:
            answer.append([song[s][0],song[s][1], cnt])
        cnt += 1
    
    # 재생시간 내림차순, 입력된 순서 오름차순 정렬
    answer.sort(key = lambda x: (-x[1], x[0]))
    # 반환
    if answer:
        return answer[0][0]
    else:
        return '(None)'