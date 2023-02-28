import sqlite3 as sq
conn = sq.connect('conf.db')
curs = conn.cursor()

zap1 = """SELECT * FROM UCHA;"""

curs.execute(zap1)
vyb = curs.fetchall()
print(vyb)

zap2 = """SELECT * FROM PERS WHERE Город ='Минск';"""
curs.execute(zap2)
vyb2 = curs.fetchall()
print(vyb2)

curs.close()
conn.close()
