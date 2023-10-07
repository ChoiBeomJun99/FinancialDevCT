# 실패.
# # 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다.
# # C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
# # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# # 조건이 일치하는 음악이 없을 때는 '(None)' 반환
# def solution(m, musicinfos):
#     answer = ''
#     howLong = {} # 각 곡의 재생된 시간 비교를 하기위한 dict
    
#     for i in musicinfos:
#         tmp = i.split(',') # 0, 1: 재생, 종료 시각 / 2: 곡이름 / 3:멜로디 루틴
        
#         start = tmp[0].split(':')
#         end = tmp[1].split(':')
    
#         # 재생된 시간 
#         howLong[tmp[2]] = (int(end[0]) - int(start[0])) * 60 + (int(end[1]) - int(start[1]))
        
#     # 본격 비교 시작
#     for i in musicinfos:
#         # 문자열 틀어진 분만큼 정제하기
#         tmp = i.split(',') # 0, 1: 재생, 종료 시각 / 2: 곡이름 / 3:멜로디 루틴
        
#         # #의 개수
#         countSharp = tmp[3].count('#')
        
#         songTime = len(tmp[3]) - countSharp # 노래의 총 길이
#         playTime = howLong[tmp[2]] # 재생된 시간
        
#         fullSequence = ""
        
#         # 계음에서 #처리를 해주어야한다.
#         if songTime >= playTime:
#             # 노래의 길이가 재생된 길이보다 크거나 같은 경우
#             fullSequence = tmp[3][0: playTime + countSharp]
#         else:
#             # 노래의 길이가 재생된 길이보다 짧은 경우
#             idx = 0
#             nowCount = 0
            
#             while nowCount < playTime:
#                 nowValue = tmp[3][idx % (songTime + countSharp)]
#                 fullSequence += nowValue
                
#                 if nowValue != '#':
#                     nowCount += 1
                
#                 idx += 1
                
#         print(fullSequence)
#         if m in fullSequence:
#             # 처리로직 필요하다
#             idx = fullSequence.find('ABC')
#             if fullSequence[idx + len(m)] == '#':
#                 continue
                
#             elif (answer == '') or (answer != '' and howLong[tmp[2]] > howLong[answer]):
#                 answer = tmp[2]
                
#     return answer


def replaceMelody(melody):
    
    if 'C#' in melody:
        melody = melody.replace('C#', 'c')
    
    if 'D#' in melody:
        melody = melody.replace('D#', 'd')
        
    if 'F#' in melody:
        melody = melody.replace('F#', 'f')
        
    if 'G#' in melody:
        melody = melody.replace('G#', 'g')
        
    if 'A#' in melody:
        melody = melody.replace('A#', 'a')
        
    return melody

def solution(m, musicinfos):
    answer = ''
    howLong = {} # 각 곡의 재생된 시간 비교를 하기위한 dict
    
    for i in musicinfos:
        tmp = i.split(',') # 0, 1: 재생, 종료 시각 / 2: 곡이름 / 3:멜로디 루틴
        
        start = tmp[0].split(':')
        end = tmp[1].split(':')
    
        # 재생된 시간 
        howLong[tmp[2]] = (int(end[0]) - int(start[0])) * 60 + (int(end[1]) - int(start[1]))
        
    m = replaceMelody(m) # m도 변화
    
    # 본격 로직 시작하기
    for i in musicinfos:
        fullMelody = ""
        start, end, name, song = i.split(',')
        
        songTime = len(song) - song.count('#') #실질적인 노래시간
        playTime = howLong[name] #재생시간
        
        #song에 대한 반복을 처리해줘야함
        song = replaceMelody(song)
        
        for i in range(0, playTime // songTime):
            fullMelody += song
        
        fullMelody += song[0:playTime % songTime]
        
        if m in fullMelody:
            if answer == '' or (answer != " " and (howLong[name] > howLong[answer])):
                answer = name
                    
    return "(None)" if answer == '' else answer

