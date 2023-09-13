#SQL(1)(노말)_과일로만든아이스크림고르기
#테이블(1) 상반기주문정보 - FIRST_HALF
#테이블(2) 성분정보 - ICECREAM_INFO ... 맛별성분

SELECT A.FLAVOR
FROM FIRST_HALF AS A LEFT JOIN ICECREAM_INFO AS B
ON A.FLAVOR = B.FLAVOR
WHERE (A.TOTAL_ORDER > 3000) AND (B.INGREDIENT_TYPE LIKE '%fruit_based%')
ORDER BY A.TOTAL_ORDER DESC;




#SQL(1)(챌린지)_서울에위치한식당목록출력
-- 코드를 입력하세요
#테이블(1) REST_INFO - 식당정보 : !!식당ID, 식당이름, 음식종류, 조회수, 즐겨찾기수, 주차장유무,
#                               주소, 전화번호
#테이블(2) REST_REVIEW - 리뷰정보 : 리뷰ID, !!식당ID, 회원ID, 점수, 리뷰텍스트, 리뷰작성일
#식당별로 여러개의 리뷰 존재하는것

SELECT B.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS,
       ROUND(AVG(A.REVIEW_SCORE),2) AS SCORE
                 #ROUND(   ,2) 일때가 셋째자리에서 반올림
FROM REST_REVIEW AS A LEFT JOIN REST_INFO AS B
ON A.REST_ID=B.REST_ID
                 #여기까지면 식당 리뷰별로 식당정보가 다 붙음
WHERE B.ADDRESS LIKE '서울%'
                 #앞에도 %이 붙으면 동서울 같은거도 나옴..
GROUP BY B.REST_ID
ORDER BY SCORE DESC, B.FAVORITES DESC;