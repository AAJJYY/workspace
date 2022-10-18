##########################
# MySQL + Python
# create table
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

cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4), userName \
    char(15), email char(20), birthYear int)")