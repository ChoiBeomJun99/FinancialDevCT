#SQL(챌린지)_취소되지않는진료예약조회하기
#테이블(B) PATIENT - 환자정보 : 환자번호, 환자이름, 성별코드, 나이, 전화번호
#테이블(C) DOCTOR - 의사정보 : 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 전화번호
#테이블(A) APPOINTMENT - 진료예약목록 : 예약일, 예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 취소날짜

SELECT C.APNT_NO, C.PT_NAME, C.PT_NO, D.MCDP_CD, D.DR_NAME, C.APNT_YMD
FROM (SELECT A.APNT_YMD, A.APNT_NO, A.MDDR_ID, A.PT_NO, B.PT_NAME,
      A.APNT_CNCL_YN, A.APNT_CNCL_YMD
      FROM APPOINTMENT AS A LEFT JOIN PATIENT AS B
      ON A.PT_NO=B.PT_NO) AS C LEFT JOIN DOCTOR AS D
ON C.MDDR_ID=D.DR_ID
WHERE (D.MCDP_CD = 'CS') AND (C.APNT_CNCL_YN = 'N')
      AND (DATE_FORMAT(C.APNT_YMD, '%Y-%m-%d')='2022-04-13')
ORDER BY C.APNT_YMD ASC;

#의사ID가 테이블별로 컬럼명이 다른거에 주의하기..