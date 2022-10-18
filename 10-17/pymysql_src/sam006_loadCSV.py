# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 14:14:47 2021

@author: 82102
"""


import csv
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1111', db='shoppingDB', charset='utf8')
cur = conn.cursor()

f = open('data.csv', 'r') # csv 파일이 utf8로 인코딩이 되어 있을 때
csvReader = list(csv.reader(f))
cur.execute("CREATE TABLE IF NOT EXISTS sba (name char(10), sex char(1), class char(1), attend char(1))")    

for data in csvReader[1:]: # csv 파일에 column명이 있다면 csvReader[1:]로 설정하고 하면 된다.
    row1 = data[0]
    row2 = data[1]
    row3 = data[2]
    row4 = data[3]

    sql = """insert into ubion (name, sex, class, attend) values(%s, %s, %s, %s);"""
    cur.execute(sql, (row1, row2, row3, row4))

f.close()
conn.commit()


'''
참고

df = df[['회사명', '종목코드', '업종']]
tmp = ""
for x in range(len(df.columns)):
    tmp = tmp + "%s,"

tmp = tmp[0:len(tmp)-1]
sql = f"insert into fnatable values({tmp})"
cur.executemany(sql, df.values.tolist())
'''