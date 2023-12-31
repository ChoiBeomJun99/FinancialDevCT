--https://school.programmers.co.kr/learn/courses/30/lessons/133027

SELECT C.FLAVOR
FROM(
    SELECT A.FLAVOR,SUM(A.TOTAL_ORDER)+SUM(B.TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF A
    JOIN JULY B ON A.FLAVOR=B.FLAVOR
    GROUP BY A.FLAVOR
    ORDER BY TOTAL_ORDER DESC
)C
WHERE ROWNUM<=3
