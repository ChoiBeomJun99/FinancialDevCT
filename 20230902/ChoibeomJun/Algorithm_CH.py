import math

# 요금 계산 함수
def calFee(fees, totalParkingTime):    
    # fees idx 별 내용
    # 0: 기본 시간 / 1: 기본 요금(원) / 2: 단위 시간(분) / 3: 단위 요금(원)
    
    tmp = []
    result = sorted(totalParkingTime)
    
    for i in result:
        parkingTime = totalParkingTime[i]
            # 누적 주차 시간이 기본 시간 이하
        if fees[0] >= parkingTime:
            tmp.append(fees[1])
    
        # 누적 주차 시간이 기본 시간 이상s
        else:
            extraTime = parkingTime - fees[0] # 초과 시간
            extraFee = math.ceil(extraTime / fees[2]) * fees[3]
        
            tmp.append(fees[1] + extraFee)
            
    return tmp

def solution(fees, records):
    answer = []
    
    totalParkingTime = {} # 각 차량 마다 주차한 시간 정산
    parkingLot = {} # 주차장 내부 차량 dict / key: 차량 번호, value: 입차 시간
    
    for info in records:
        time, carNum, inOut = info.split(" ") # 0: 시간 / 1: 차량 번호 / 2: 입출차 정보
        
        if inOut == "IN":
            # 입차
            parkingLot[carNum] = time # 주차장에 넣어주기 (차량 번호: 입차 시간)
            continue
        else:
            # 출차
            inTime = parkingLot[carNum].split(":") # 입차 시간
            outTime = time.split(":") # 출차 시간
            
            parkingTime = (int(outTime[0]) - int(inTime[0])) * 60  + (int(outTime[1]) - int(inTime[1]))
            
            totalParkingTime[carNum] = totalParkingTime.get(carNum, 0) + parkingTime
            parkingLot.pop(carNum)
            
    
    for key, value in parkingLot.items():
        inTime = value.split(":")
        parkingTime = (23 - int(inTime[0])) * 60  + (59 - int(inTime[1]))
        
        totalParkingTime[key] = totalParkingTime.get(key, 0) + parkingTime
        
    
    answer = calFee(fees, totalParkingTime)
    return answer