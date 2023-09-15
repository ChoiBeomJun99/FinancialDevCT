def solution(food):
    tmp = ''
    for i in range(1, len(food)):
        tmp += str(i) * (food[i]//2)
    return tmp + '0' + tmp[::-1]