def solution(m, musicinfos):
    answer = []

    for i in range(0, len(musicinfos)):
        music = musicinfos[i].split(",")
        time = int(("").join(music[1].split(":"))) - int(("").join(music[0].split(":")))
        mm = music[3] * 10
        mm = mm[0:time]

        if (
            mm.find(m) != -1
            and mm[mm.find(m) + len(m) : mm.find(m) + len(m) + 1] != "#"
        ):
            answer = music[2]

    if not answer:
        answer = "(None)"

    return answer


#####


# '#'이 붙은 음을 소문자로 변환하는 함수
def change(music):
    if "A#" in music:
        music = music.replace("A#", "a")
    if "F#" in music:
        music = music.replace("F#", "f")
    if "C#" in music:
        music = music.replace("C#", "c")
    if "G#" in music:
        music = music.replace("G#", "g")
    if "D#" in music:
        music = music.replace("D#", "d")
    return music


def solution(m, musicinfos):
    answer = []
    index = 0  # 먼저 입력된 음악을 판단하기 위해 index 추가
    for info in musicinfos:
        index += 1
        music = info.split(",")
        start = music[0].split(":")  # 시작 시간
        end = music[1].split(":")  # 종료 시간
        # 재생시간 계산
        time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))

        # 악보에 #이 붙은 음을 소문자로 변환
        changed = change(music[3])

        # 음악 길이
        a = len(changed)

        # 재생시간에 재생된 음
        b = changed * (time // a) + changed[: time % a]

        # 기억한 멜로디도 #을 제거
        m = change(m)

        # 기억한 멜로디가 재생된 음에 있다면 결과배열에 [시간, index, 제목]을 추가
        if m in b:
            answer.append([time, index, music[2]])

    # 결과배열이 비어있다면 "None" 리턴
    if not answer:
        return "(None)"
    # 결과배열의 크기가 1이라면 제목 리턴
    elif len(answer) == 1:
        return answer[0][2]
    # 결과 배열의 크기가 2보다 크다면 재생된 시간이 긴 음악, 먼저 입력된 음악순으로 정렬
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]  # 첫번째 제목을 리턴
