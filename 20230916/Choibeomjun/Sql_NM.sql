SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O LEFT JOIN ANIMAL_INS I ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY (O.DATETIME - I.DATETIME) DESC
LIMIT 2