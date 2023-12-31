#SQL(2)_노말_자동차 대여 기록에서 장기/단기 대여 구분하기
#틀린답변
SELECT HISTORY_ID, CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       END_DATE - START_DATE + 1,
       CASE WHEN (END_DATE - START_DATE + 1)>=30 THEN '장기 대여' ELSE '단기 대여' END AS RENT_TYPE
       #날짜 계산할때, 단순히 - 를 사용하면 제대로 되지 않는 경우도 잇음
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE (DATE_FORMAT(START_DATE,'%y-%m')='22-09')
ORDER BY HISTORY_ID DESC;

#정답
SELECT HISTORY_ID, CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN DATEDIFF(END_DATE,START_DATE)+1 >=30 THEN '장기 대여'
            ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE (DATE_FORMAT(START_DATE,'%y-%m')='22-09')
ORDER BY HISTORY_ID DESC;

#기억하기
#(1) 걍 날짜-날짜 방식은 오류발생가능
#(2) DATEDIFF(끝날짜, 시작날짜), 이때 3월1일 - 3월1일 은 0으로 반환됨