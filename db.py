import sqlite3 as sql 

conect = sql.connect ('form_db.db')
cursor = conect.cursor()


sql = """CREATE TABLE IF NOT EXISTS "usuarios" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" varchar(30),
    "senha" varchar(30)

    )"""

cursor.execute(sql)
conect.commit()
cursor.close()