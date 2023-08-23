def solution(record):
    answer = []
    name_dict = {}
    words = [w.split() for w in record]

    for word in words:
        if word[0] == "Enter" or word[0] == "Change":
            name_dict[word[1]] = word[2]

    for word in words:
        if word[0] == "Enter":
            answer.append(name_dict[word[1]] + "님이 들어왔습니다.")
        elif word[0] == "Leave":
            answer.append(name_dict[word[1]] + "님이 나갔습니다.")
    return answer
