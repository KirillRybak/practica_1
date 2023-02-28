
import sqlite3 as sql
conn=sql.connect('update.db')
curs=conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS PERS ('ФИО' TEXT,'Учёная_степень' TEXT,'Научное_направление' TEXT,'Место_работы' TEXT,'Кафедра' TEXT,'Должность' TEXT,'Страна' TEXT,'Город' TEXT,'Адрес' TEXT,'Рабочий_телефон' TEXT);""")
conn.commit()
zap2="""INSERT INTO PERS VALUES(?,?,?,?,?,?,?,?,?,?)"""
tuple1=('Зубков Глеб Степанович','Есть','Математика','Школа','6А','Преподаватель(изменено)','Беларусь','Минск','Ул.Победы','987654321')
#curs.execute(zap2,tuple1)
zap1 ="""UPDATE PERS SET ФИО='Ильина Ульяна Артёмовна(изменено)' WHERE Научное_направление='Психология' ;"""
curs.execute(zap1)
conn.commit()
zap3="""DELETE FROM PERS WHERE Кафедра='6А';"""
curs.execute(zap3)
conn.commit()
curs.close()
conn.close()
