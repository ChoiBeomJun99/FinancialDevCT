#SQL(1)_노말_재구매가일어난상품과회원리스트구하기
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
#재구매한 고객만 찾는 것이 아니라, 동일한 상품 재구매 여부를 찾는 것이므로!
HAVING COUNT(*)>1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;


#SQL(1)_챌린지_보호소에서 중성화한 동물
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_OUTS AS A LEFT JOIN (SELECT ANIMAL_ID, SEX_UPON_INTAKE
                                 FROM ANIMAL_INS
                                 WHERE SEX_UPON_INTAKE LIKE '%Intact%') AS B
                                 #들어왔을때 중성화되어있지 않은(Intact 포함) 동물들만 찾기
ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE (B.SEX_UPON_INTAKE IS NOT NULL) AND REGEXP_LIKE(A.SEX_UPON_OUTCOME, 'Neutered|Spayed')
      #들어왔을때 중성화X                   #LIKE에 대한 여러 조건 달기!
ORDER BY A.ANIMAL_ID;