#SQL(챌린지)_조회수가가장많은중고거래게시판의첨부파일조회하기
#풀이시간 : 15분
#테이블(1) USED_GOODS_BOARD - 중고거래 게시판 정보 : BOARD_ID, WRITER_ID, TITLE, CONTENTS,
#                                                PRICE, CREATED_DATE, STATUS, VIEWS
#테이블(2) USED_GOODS_FILE - 중고거래 게시판 첨부파일 정보 : FILE_ID, FILE_EXT(확장자),
#                                                       FILE_NAME, BOARD_ID
#이때 첨부된 파일이 여러개일수잇음...

#조회수제일높은거 일단 찾기
# SELECT BOARD_ID FROM USED_GOODS_BOARD
# WHERE VIEWS=(SELECT MAX(VIEWS) FROM USED_GOODS_BOARD);

SELECT CONCAT('/home/grep/src/',BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID=(SELECT BOARD_ID FROM USED_GOODS_BOARD 
                WHERE VIEWS=(SELECT MAX(VIEWS) FROM USED_GOODS_BOARD))
ORDER BY FILE_ID DESC;

#몰랐던점!!! CONCAT함수가 기억이 안나서 구글링...
#CONCAT 함수 >> 문자열합쳐서 새로운컬럼 생성 함수
#CONCAT_WS 함수 >> CONCAT_WS('구분자',컬럼1, 컬럼2)이면 컬럼1구분자컬럼2 생성

#꿀팁 FROM 국민코테 ㅠ
#GROUP_CONCAT 함수 >> GROUP BY로 묶인 그룹에 속한 특정컬럼값들을 하나의 문자열로 합쳐줌



#SQL(노말)_모든레코드조회하기
#풀이시간 : 5초
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;