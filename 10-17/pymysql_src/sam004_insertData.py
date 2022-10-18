##########################
# MySQL + Python
# Insert Data
# Create by shamantha
##########################


import pymysql

# 전역변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql=""

# 메인 코드
conn = pymysql.connect(host='localhost', user='root', password='1111', db='shoppingDB', charset='utf8')
cur = conn.cursor()

cur.execute("INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('kim', 'kim mike', 'kim@naver.com', 1980)")
cur.execute("INSERT INTO userTable VALUES('park', 'park minseo', 'park@naver.com', 2000)")

conn.commit()
conn.close()

'''
df = df[['회사명', '종목코드', '업종']]
tmp = ""
for x in range(len(df.columns)):
    tmp = tmp + "%s,"

tmp = tmp[0:len(tmp)-1]
sql = f"insert into fnatable values({tmp})"
cur.executemany(sql, df.values.tolist())
'''