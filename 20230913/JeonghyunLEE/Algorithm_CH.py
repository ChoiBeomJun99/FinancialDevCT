# https://school.programmers.co.kr/learn/courses/30/lessons/17686

# 정규표현식 라이브러리
import re

def solution(files):
    answer = []
    # 1) 정렬 : 파일의 header, 파일의 number, 원본의 순서
    my_files = []

    # 2) 입력 files를 돌아가면서, header(대소문자 통일)와 number part(0 패딩 처리 : int 형 변환 사용) 처리.
    for idx, i in enumerate(files):
      # 2-1) number 파트 추출 : re
      number = re.findall("\d+", i)[0] # 숫자 파트 추출
      # 2-2) header 파트 : number 나타나기 직전으로 slicing
      head = i[ : i.index(number)]
      # 2-3) number, head 처리
      number = int(number) # 0 패딩 제거
      head = head.lower() # 소문자 통일
      # 2-4) my_files에 처리
      my_files.append([head, number, idx])

    # 3) my_files를 대상으로 정렬의 기준 key
    my_files.sort(key = lambda x : (x[0], x[1])) 

    # 4) 입력 받은 files의 이름으로 출력하기
    answer = [ files[j[2]] for j in my_files ]

    return answer