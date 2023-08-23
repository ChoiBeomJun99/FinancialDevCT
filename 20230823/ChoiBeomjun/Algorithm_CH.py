def solution(record):
    answer = []
    
    # dictionary 자료구조를 이용하여 풀이 제시. uid에 해당하는 이름정보를 제공.
    dictionary = {} 
    
    # 본격 문장 하나씩 처리하기 시작.
    for i in record:
        mes = i.split(" ")
        
        func = mes[0] # 동작
        uid = mes[1] # 유저아이디
        
        answer.append([func, uid]) # 동작과 uid를 저장 (답을 위함.)
        if func == "Enter":
            # 입장
            dictionary[uid] = mes[2]
        elif func == "Change":
            # 변경
            dictionary[uid] = mes[2]
            
    result = []
    
    for i in answer: 
        action = i[0]
        name = dictionary[i[1]]
        
        if action == "Enter":
            result.append(name+ "님이 들어왔습니다.")
        elif action == "Leave":
            result.append(name+ "님이 나갔습니다.")
        
    return result