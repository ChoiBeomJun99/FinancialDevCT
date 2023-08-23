def solution(record):
    ids = []
    answer = []
    users = {}
    for r in record:
        command = r.split()
        c = command[0]
        uid = command[1]
        if c == "Enter":
            users[uid] = command[2]
            ids.append(uid)
            answer.append(command[2]+"님이 들어왔습니다.")
        elif c == "Leave":
            ids.append(uid)
            answer.append(users[uid]+"님이 나갔습니다.")
        else:
            users[uid] = command[2]
    for i in range(len(ids)):
        username = users[ids[i]]
        if answer[i][len(answer[i]) - 7:] == "들어왔습니다.":
            answer[i] = username + "님이 들어왔습니다."
        else:
            answer[i] = username + "님이 나갔습니다."
    return answer
