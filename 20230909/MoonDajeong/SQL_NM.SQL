#테이블 정보를 보면, OPTIONS 자체가 VARCHAR로 입력되어있는 문자열임! > LIKE 사용
SELECT *
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;