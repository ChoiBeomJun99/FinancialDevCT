SELECT rest_review.REST_ID,rest_info.REST_NAME,rest_info.FOOD_TYPE,rest_info.FAVORITES,rest_info.ADDRESS,ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM rest_review,rest_info
WHERE rest_review.rest_id=rest_info.rest_id AND ADDRESS LIKE '서울%'
GROUP BY rest_review.rest_id
ORDER BY SCORE DESC, FAVORITES DESC