# 비밀지도
def solution(n, arr1, arr2):
    answer = []

    for idx in range(len(arr1)):
        arr1_bi = bin(arr1[idx])[2:].zfill(n)
        arr2_bi = bin(arr2[idx])[2:].zfill(n)

        tmp = ""
        for i in range(n):
            if arr1_bi[i] == "1" or arr2_bi[i] == "1":
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)

    return answer
