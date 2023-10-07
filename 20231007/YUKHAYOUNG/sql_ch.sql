SELECT id, nickname, address, phone
FROM (
        SELECT user.user_id AS id, user.nickname AS nickname
            , CONCAT(city, ' ',street_address1, ' ',street_address2) AS address
            , CONCAT(substr(TLNO,1,3), '-', substr(TLNO,4,4), '-', substr(TLNO,8,4)) AS phone
            , COUNT(*) AS user_count
        FROM used_goods_user AS user
            INNER JOIN used_goods_board AS board ON user.user_id = board.writer_id
        GROUP BY user.user_id
    ) user
WHERE user_count > 2
ORDER BY id DESC