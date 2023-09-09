def solution(s):
    numDict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", 
              "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}  
    answer = s
    
    for key, value in numDict.items():
        answer = answer.replace(key, value)
    return int(answer)