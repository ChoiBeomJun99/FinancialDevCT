-- https://school.programmers.co.kr/learn/courses/30/lessons/144856

SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY,
       SUM((BS.SALES * B.PRICE)) as TOTAL_SALES
FROM BOOK as B
    JOIN AUTHOR as A
    ON B.AUTHOR_ID = A.AUTHOR_ID
    JOIN BOOK_SALES as BS
    ON B.BOOK_ID = BS.BOOK_ID
WHERE SALES_DATE like '2022-01%'
GROUP BY A.AUTHOR_NAME, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC