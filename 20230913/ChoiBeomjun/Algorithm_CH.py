def solution(files):
    answer = []
    head, number, tail = '', '', ''

    for file in files:
        # HEAD, NUMBER, TAIL 분리 과정        
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                
                # TAIL 분리 과정
                for j in range(len(number)):
                    if not number[j].isdigit() and j < 5:
                        tail = number[j:]
                        number = number[:j]
                        break
                    elif j >= 5:
                        tail = number[5:]
                        number = number[:5]
                        break
                    
                answer.append([head, number, tail])
                head, number, tail = '', '', ''
                break
    
    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]