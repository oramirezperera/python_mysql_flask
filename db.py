import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin',
    database = 'pruebaudemy'
) # This code it is not recommended to be harcoded here because of the host, user and password in plain view, 
# for security is recommended to create a config.py file and import it

cursor = mydb.cursor()

#showing data
# cursor.execute('select * from usuario')
# resultado = cursor.fetchall() # If you use fetchone() brings only the first result
# print(resultado)

#see the definition of a table
# cursor.execute('show create table usuario')

#insert data
#sql = 'insert into usuario (email, username, edad) values (%s, %s, %s)'
#values = ('micorreo@correo.co.nz', 'nombreusuario', 45)
#cursor.execute(sql, values)
#cursor.execute('select * from usuario')
#mydb.commit()
#print(cursor.rowcount)

#update data
# sql = 'update usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 4)
# cursor.execute(sql, values)
# mydb.commit()
#resultado = cursor.fetchall() 

#delete data
# sql = 'delete from usuario where id = %s'
# values = (4, ) # the comma is a requisite
# cursor.execute(sql, values)
# mydb.commit()

#limit rows
# cursor.execute('select * from usuario limit 1')
# resultado = cursor.fetchall() # If you use fetchone() brings only the first result
# print(resultado)