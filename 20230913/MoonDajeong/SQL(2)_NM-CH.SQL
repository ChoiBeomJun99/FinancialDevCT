#SQL(2)(노말)_있었는데요없었습니다
#테이블(1) ANIMAL_INS - 들어온동물정보 : 동물ID, 생물종, 보호시작일, 시작시상태, 이름, 성별중성화
#테이블(2) ANIMAL_OUTS - 입양보낸동물정보 : 동물ID, 생물종, 입양일, 이름, 성별중성화
# 들어온동물정보 > 입양보낸동물정보

#틀린답 - DATEDIFF만 사용하면 일단위 계산밖에 안됨
# SELECT A.ANIMAL_ID, A.NAME
# FROM ANIMAL_INS AS A LEFT JOIN ANIMAL_OUTS AS B
# ON A.ANIMAL_ID=B.ANIMAL_ID
# #입양보낸기록 다 붙여짐
# WHERE (B.DATETIME IS NOT NULL) #입양보내진동물이면서
#       AND (DATEDIFF(B.DATETIME, A.DATETIME)<=0) #시간-초까지 계산해야되는데...
# ORDER BY A.DATETIME ASC;
# #날짜는 옛날 < 최근 이므로 옛날꺼부터 정렬이면 오름차순

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE (B.DATETIME IS NOT NULL) AND
      (TIMESTAMPDIFF(SECOND, A.DATETIME, B.DATETIME) <= 0)
      # TIMESTAMPDIFF 함수 주의! 뒤-앞 으로 옵션이계산됨
ORDER BY A.DATETIME ASC;

#기억할정보
#DATEDIFF(날짜1, 날짜2) : (날짜1-날짜2) 에 대해서 일 수를 반환
#TIMESTAMPDIFF(기준, 날짜1, 날짜2) : (날짜2-날짜1) 에 대해서 기준대로 반환
#                                   SECOND(초), MINUTE(분), HOUR(시간), DAY(일)





#SQL(2)(챌린지)_5월식품들의총매출구하기
#테이블(B) FOOD_PRODUCT - 식품정보 : 식품ID, 이름, 코드, 분류, 가격
#테이블(A) FOOD_ORDER - 식품주문정보 : 주문ID, 식품ID, 주문량, 생산일자, 입고일자, 출고일자,
#                                   공장ID, 창고ID
#주문정보 > 식품정보

SELECT B.PRODUCT_ID, B.PRODUCT_NAME, SUM(A.AMOUNT)*B.PRICE AS TOTAL_SALES
                #총매출이면,,, 가격*수량인거 ,, 잊지말기,,
FROM FOOD_ORDER AS A LEFT JOIN FOOD_PRODUCT AS B
ON A.PRODUCT_ID=B.PRODUCT_ID
                #여기까지 주문정보별로 식품기본정보 붙음
WHERE DATE_FORMAT(A.PRODUCE_DATE, '%Y-%m')='2022-05'
GROUP BY A.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, B.PRODUCT_ID ASC;