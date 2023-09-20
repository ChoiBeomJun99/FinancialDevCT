-- 코드를 입력하세요
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')

GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) = 2 
--point : Distinct : 상품 종류에 distinct를 취하여, 중복을 제거.
ORDER BY CART_ID;