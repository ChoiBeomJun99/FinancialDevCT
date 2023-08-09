
def solution(progresses, speeds):
    answer = []
    while len(progresses)!=0:
      for i in range(0,len(progresses)):
        progresses[i]+=speeds[i]
      
      k=0
      n=0
  
      while True:
        if progresses[k] >= 100:
          del progresses[k]
          del speeds[k]
          n+=1
          if len(progresses) == 0:
            break;
        else :
          break;

      if n!=0:
        answer.append(n)
    return answer
