-- https://school.programmers.co.kr/learn/courses/30/lessons/164670

-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소', concat(SUBSTR(TLNO,1,3), '-', SUBSTR(TLNO,4,4), '-', SUBSTR(TLNO,8)) as '전화번호'
FROM USED_GOODS_BOARD B
    JOIN USED_GOODS_USER U
    ON B.WRITER_ID = U.USER_ID
GROUP BY USER_ID
HAVING count(USER_ID) >= 3
ORDER BY USER_ID DESC