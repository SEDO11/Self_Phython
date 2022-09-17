import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000',db='solodb', charset='utf8')

cur = conn.cursor() # sql 실행 결과를 받는 인자

data = { '아이디':None, '이름':None, '이메일':None, '출생연도':None}

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id CHAR(4), username CHAR(15), email CHAR(20), birthYear INT)")

try:
    # sql SELECT문 선언
    sql = f"SELECT * FROM userTable"
    cur.execute(sql)
    
    print('ID       이름      이메일      출생연도')
    print('--------------------------------------')
    while True:
        row = cur.fetchone()
        if row == None:
            break
        data['아이디'] = row[0]
        data['이름'] = row[1]
        data['이메일'] = row[2]
        data['출생연도'] = row[3]
        print(f'{data["아이디"]}    {data["이름"]}  {data["이메일"]}    {data["출생연도"]}')
except:
    print('에러가 발생하였습니다.')
finally:
    conn.close() # db 닫기