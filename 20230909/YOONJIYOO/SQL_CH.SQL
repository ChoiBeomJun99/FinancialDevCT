-- 코드를 입력하세요
/* 
1. A.CAR_ID=B.CAR_ID에서 대여한 날을 계산 후 추출 -> T0_DATE(END_DATE)-TO_DATE(START_DATE) AS PERIOD
2. A.CAR_TYPE=C.CAR_TYPE JOIN 후, 
7일이상 CASE => 7<=PERIOD<30 
30일이상 30<=PERIOD<90 
90일이상 90<=PERIOD

생각해보고 다시 풀어보기 
*/