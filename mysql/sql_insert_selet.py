import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3310, user='root', password='0000',db='solodb', charset='utf8')

cur = conn.cursor() # sql 실행 결과를 받는 인자

# 테이블 생성
# cur.execute("DROP TABLE IF EXISTS userTable")
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id CHAR(4), username CHAR(15), email CHAR(20), birthYear INT)")

data = { '아이디':None, '이름':None, '이메일':None, '태어난 해':None}

def insert():
    global data
    for key in data.keys():
        print(key, ':', end=' ')
        data[key] = input()

    try:
        # sql 생성문 선언
        sql = f"SELECT * FROM userTable WHERE id = '{data.get('아이디')}'"
        cur.execute(sql)
        
        if 1 > cur.execute(sql): # 일치하는 아이디가 없으면
            sql = f"INSERT INTO userTable VALUES('{data.get('아이디')}', '{data.get('이름')}', '{data.get('이메일')}', {data.get('태어난 해')})"
            cur.execute(sql)
            print('저장되었습니다.')
            conn.commit() # 완전히 저장
        else:
            print('중복되는 아이디가 있어서 회원가입이 되지 않았습니다.')
    except:
        print('에러가 발생하였습니다.')

def select():
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
            data['태어난 해'] = row[3]
            print(f'{data["아이디"]}    {data["이름"]}  {data["이메일"]}    {data["태어난 해"]}')
    except:
        print('에러가 발생하였습니다.')
        
def delete():
    print('삭제할 회원의 아이디를 입력하세요')
    uid = input()
    try:
        sql = f"SELECT * FROM userTable WHERE id = '{uid}'"
        if 0 < cur.execute(sql): # 일치하는 아이디가 있으면
            sql = f"DELETE FROM userTable WHERE id = '{uid}'"
            cur.execute(sql)
            conn.commit() # 완전히 저장
            print('해당 아이디의 회원 정보를 삭제 했습니다.')
        else:
            print('해당 아이디와 일치하는 회원 정보가 없습니다.')
    except:
        pass
        
while True:
    print('1: select | 2: insert | 3: delete | q: 종료')
    s = input()
    if s == '1':
        select()
    elif s == '2':
        insert()
    elif s == '3':
        delete()
    elif s == 'q' or 'Q':
        conn.close() # db 닫기
        break