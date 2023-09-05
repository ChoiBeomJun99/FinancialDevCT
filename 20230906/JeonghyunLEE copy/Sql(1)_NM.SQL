-- https://school.programmers.co.kr/learn/courses/30/lessons/131534

-- 코드를 입력하세요
SELECT DATE_FORMAT(O.SALES_DATE, '%Y') as YEAR, DATE_FORMAT(O.SALES_DATE, '%m') as MONTH, count(distinct U.user_id) as PUCHASED_USERS,
ROUND( count(distinct U.user_id) / (SELECT COUNT(distinct U.user_id) FROM USER_INFO U WHERE U.JOINED like '2021%'), 1) as PUCHASED_RATIO
FROM USER_INFO U JOIN
    ONLINE_SALE O
    ON U.USER_ID = O.USER_ID
WHERE U.JOINED like '2021%'
GROUP BY YEAR, MONTH