SELECT m.member_name, r.review_text, date_format(r.review_date, "%Y-%m-%d")
FROM member_profile m

INNER JOIN (
    SELECT *
    FROM rest_review 

    WHERE member_id in (
        SELECT member_id 
        FROM rest_review
        GROUP BY member_id
        HAVING count(*) = (

            SELECT count(*)
            FROM rest_review
            GROUP BY member_id
            ORDER BY count(*) desc
            LIMIT 1
        )
    )
) r
ON m.member_id = r.member_id
ORDER BY r.review_date, r.review_text
