-- https://school.programmers.co.kr/learn/courses/30/lessons/131118

-- 코드를 입력하세요
SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, round(avg(R.REVIEW_SCORE), 2) as SCORE
FROM REST_INFO as I
    Inner Join REST_REVIEW as R
    on I.REST_ID = R.REST_ID
WHERE ADDRESS like ('서울%')
Group By REST_NAME
Order By SCORE DESC, FAVORITES DESC