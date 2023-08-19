def Max(set1, set2):
    if len(set1) > len(set2):
        return set1
    else:
        return set2

def Min(set1, set2):
    if len(set1) > len(set2):
        return set2
    else:
        return set1

def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []
    inter = []
    sum = []

    # set1 = [str1[i:i+2] for i in range(0, len(str1), 2)]
    for i in range(0, len(str1)-1):
        if str1[i:i+2].isalpha():
            set1.append(str1[i:i+2].lower())
    for i in range(0, len(str2)-1):
        if str2[i:i+2].isalpha():
            set2.append(str2[i:i+2].lower())

    for i in Max(set1, set2):
        sum.append(i)
    for i in Min(set1, set2):
        if i not in sum:
            sum.append(i)

    min_copy = Min(set1, set2).copy()
    max_copy = Max(set1, set2).copy()

    for i in min_copy: #교집합
        if i in max_copy:
            inter.append(i)
            max_copy.remove(i)

    if len(inter) == 0 and len(inter) == 0:
        answer = 65536
    else:
        answer = len(inter)/len(sum)*65536

    print(set1)
    print(set2)
    return int(answer)
