#SQL(CH)_상품을구매한회원비율구하기

SELECT YEAR(A.SALES_DATE) AS YEAR, MONTH(A.SALES_DATE) AS MONTH,
       COUNT(DISTINCT A.USER_ID) AS PUCHASED_USERS,
       ROUND(COUNT(DISTINCT A.USER_ID)/(SELECT COUNT(DISTINCT USER_ID)
                                        FROM USER_INFO
                                        WHERE YEAR(JOINED)=2021),1) AS PUCHASED_RATIO
FROM ONLINE_SALE AS A LEFT JOIN USER_INFO AS B
ON A.USER_ID=B.USER_ID
WHERE YEAR(B.JOINED)=2021
GROUP BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE)
ORDER BY 1,2;

#새로알게된것
#(1) ORDER BY로 정렬을 YEAR, MONTH 지정해줫어야햇는데 있는함수명이라 안된댓음 >> 1,2로 해결
#(2) 서브쿼리로 스칼라값 구해서 비율구함