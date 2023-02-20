import sqlite3

con = sqlite3.connect('conf.db')
cur = con.cursor()

zop2 = """CREATE TABLE IF NOT EXISTS PERS ('Ф.И.О.' TEXT,'Учёная степень' TEXT,'Научное направление' TEXT,'Место работы' TEXT,'Кафедра' TEXT,'Должность' TEXT,'Страна' TEXT,'Город' TEXT,'Адрес' TEXT,'Рабочий телефон' TEXT);"""

cur.execute(zop2)
con.commit()
zop3 = """CREATE TABLE IF NOT EXISTS UCHA ('Докладчик или участник' TEXT,'Дата рассылки приглашения' TEXT,'Дата поступления заявки' TEXT,'Тема доклада' TEXT,'Отметка о поступлении тезисов' TEXT,'Дата приезда' TEXT,'Потребность в гостинице' TEXT,'Дата отъезда' TEXT);"""
cur.execute(zop3)
con.commit()
zop4 = """CREATE TABLE IF NOT EXISTS INFO ('Название конференции' TEXT,'Дата проведения' INTEGER,'Место проведения' TEXT,'Организаторы' TEXT,'Спонсоры' TEXT,'Кол-во дней конференции' INTEGER,'Кол-во участников' INTEGER,'Кол-во докладчиков' INTEGER);"""
cur.execute(zop4)
con.commit()
Z1 = """INSERT INTO INFO ('Дата проведения','Место проведения','Организаторы','Кол-во дней конференции') VALUES ('1,1,20','Р.Д.К','Есть',6); """
con.execute(Z1)
con.commit()

cur.close()
con.close()