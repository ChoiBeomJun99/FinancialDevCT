-- https://school.programmers.co.kr/learn/courses/30/lessons/133027

-- 코드를 입력하세요

SELECT F.FLAVOR
FROM FIRST_HALF F
    JOIN JULY J
    ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY sum(F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
limit 3