-- 코드를 입력하세요
#SELECT min(PRICE >= 0 and PRICE <= 10000) as PRICE_GROUP, 

#가격 대 별로 쪼개는 방법
# 1. 가격의 맨 앞자리 즉, 최대 가격 수만 뽑아내고, (이를 위해 /, FLOOR함수 사용)
# 곱하기 10000(가격대) 하면서 돌리기...
# => 이렇게 하면 자동으로 가격대가 잘림
/*
SELECT FLOOR(PRICE/10000) *10000 as PRICE_GROUP,
    count(PRODUCT_ID) as PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP*/





SELECT FLOOR(PRICE/10000)*10000 as PRICE_GROUP, 
count(PRODUCT_ID) as PRODUCTS

FROM PRODUCT

GROUP BY PRICE_GROUP

ORDER BY PRICE_GROUP