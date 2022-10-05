import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3310, user='root', password='0000',db='solodb', charset='utf8')

cur = conn.cursor() # sql 실행 결과를 받는 인자

# 테이블 생성
# cur.execute("DROP TABLE IF EXISTS userTable")
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id CHAR(4), username CHAR(15), email CHAR(20), birthYear INT)")

data = { '아이디':None, '이름':None, '이메일':None, '태어난 해':None}

for key in data.keys():
    print(key, ':', end=' ')
    data[key] = input()

try:
    # sql 생성문 선언
    sql = f"INSERT INTO userTable VALUES('{data.get('아이디')}', '{data.get('이름')}', '{data.get('이메일')}', {data.get('태어난 해')})"

    # 데이터 임시 저장
    print( '저장되었습니다.' if cur.execute(sql) > 0 else '저장되지 않았습니다.')

    conn.commit() # 완전히 저장
except:
    print('에러가 발생하였습니다.')
finally:
    conn.close() # db 닫기