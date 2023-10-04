#SQL(1)(챌린지)_자동차 대여기록별 대여 금액 구하기
#테이블(B) CAR_RENTAL_COMPANY_CAR 대여중인자동차정보 : CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
#          CAR_TYPE에는 '세단','SUV','승합차','트럭','리무진'
#          OPTIONS에는 키워드리스트로 존재, '주감센','스키','네비','통풍','열선','후방카','가죽'
#                      결국은 문자열로 들어가있음
#테이블(A) CAR_RENTAL_COMPANY_RENTAL_HISTORY 자동차대여기록정보
#          HISTORY_ID, CAR_ID, START_DATE, END_DATE
#테이블(3) CAR_RENTAL_COMPANY_DISCOUNT_PLAN 자동차종류별/대여기간종류별 할인정책정보
#          PLAN_ID, CAR_TYPE, DURATION_TYPE, DISCOUNT_RATE
#          할인률 적용 가능 대여기간종류 - (7일이상30일미만), (30일이상 90일미만), (90일이상)

#풀이시간 : 30분 정도?
#기억할거,,,, 1. 할인률이면 지불금액은 (1-할인률).......바보임?
#            2. TIMESTAMPDIFF 함수는 같은날-같은날이면 0으로 출력, 1 더해줘야함
#            3. 조인할때 테이블 별칭 잘 정하기
#            4. 조인할때 쓸데없는 컬럼도 있으면 데이터 이상해짐~필요한거만 넣기
#            5. 소수점 버리는 함수는 FLOOR( )

SELECT C.HISTORY_ID,
       CASE WHEN D.DISCOUNT_RATE IS NULL THEN (C.DAILY_FEE*C.CARDAY)
       ELSE FLOOR(C.DAILY_FEE*C.CARDAY*(100-D.DISCOUNT_RATE)*0.01) END AS FEE
FROM  (SELECT A.HISTORY_ID, B.DAILY_FEE,
      TIMESTAMPDIFF(DAY, A.START_DATE, A.END_DATE)+1 AS CARDAY,
      CASE WHEN (TIMESTAMPDIFF(DAY, A.START_DATE, A.END_DATE)+1 BETWEEN 7 AND 29) THEN '7일 이상'
           WHEN (TIMESTAMPDIFF(DAY, A.START_DATE, A.END_DATE)+1 BETWEEN 30 AND 89) THEN '30일 이상'
           WHEN (TIMESTAMPDIFF(DAY, A.START_DATE, A.END_DATE)+1 >= 90) THEN '90일 이상'
           ELSE '7일 미만' END AS DURATION_TYPE
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS A LEFT JOIN CAR_RENTAL_COMPANY_CAR AS B
      ON A.CAR_ID=B.CAR_ID WHERE B.CAR_TYPE = '트럭') AS C LEFT JOIN (SELECT DURATION_TYPE, DISCOUNT_RATE
                                                                     FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                     WHERE CAR_TYPE='트럭') AS D
ON C.DURATION_TYPE=D.DURATION_TYPE
ORDER BY FEE DESC, C.HISTORY_ID DESC;