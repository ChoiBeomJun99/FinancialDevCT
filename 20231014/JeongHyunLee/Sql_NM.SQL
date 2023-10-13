-- https://school.programmers.co.kr/learn/courses/30/lessons/59411

select I.ANIMAL_ID, I.NAME
from ANIMAL_INS I
    join ANIMAL_OUTS O
    on I.ANIMAL_ID = O.ANIMAL_ID
order by (O.DATETIME - I.DATETIME) desc
limit 2