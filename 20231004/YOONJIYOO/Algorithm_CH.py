""" 
#시간초과 실패
def solution(sequence, k):
    answer = []  # 결과를 저장할 리스트
    min_length = float('inf')  # 가장 짧은 부분 리스트의 길이를 추적할 변수
    start_index = 0  # 부분 리스트의 시작 인덱스

    for i in range(0, len(sequence)):
        result = 0
        for j in range(i, len(sequence)):
            result += sequence[j]
            
            # 부분 리스트의 합이 k와 같아지면서 가장 짧은 경우를 찾음
            if result == k:
                end_index = j  # 부분 리스트의 끝 인덱스
                if (end_index - i) < min_length:
                    min_length = end_index - i
                    start_index = i  # 가장 짧은 부분 리스트의 시작 인덱스 갱신

    if min_length != float('inf'):
        answer.extend([start_index, start_index + min_length])

    return answer
    """

# 투 포인터


def solution(sequence, k):
    n = len(sequence)

    result = 0  # 합
    end_idx = 0
    diff = n  # start_idx와 end_idx의 차이

    for start_idx in range(n):
        while result < k and end_idx < n:
            result += sequence[end_idx]
            end_idx += 1
        if result == k and end_idx - 1 - start_idx < diff:
            answer = [start_idx, end_idx - 1]
            diff = end_idx - 1 - start_idx
        result -= sequence[
            start_idx
        ]  # 현재 부분 리스트의 합에서 가장 앞에 있는 요소를 제거=>시작 인덱스 start_idx를 하나 이동한 것과 같음

    return answer
