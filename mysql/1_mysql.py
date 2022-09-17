# 사용 방법은 mysql과 동일해서 port 번호만 바꿔주면 됨

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', port=3310, db='test', charset='utf8')

cur = conn.cursor() # sql 실행 결과를 받는 인자

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id CHAR(4), username CHAR(15), email CHAR(20), birthYear INT)")

# 데이터 임시 저장
print(cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)"))
print(cur.execute("INSERT INTO userTable VALUES('kim', '김태연', 'kim@daum.net', 2011)"))
print(cur.execute("INSERT INTO userTable VALUES('star', '별사랑', 'star@paren.com', 1990)"))
print(cur.execute("INSERT INTO userTable VALUES('yang', '양지은', 'yang@gmail.com', 1993)"))

conn.commit() # 완전히 저장
conn.close() # db 닫기s