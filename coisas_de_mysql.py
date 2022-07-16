import mysql.connector
#creando nuestro diccionario
dato={
    'user':'root',
    'password':'',
    'database':'TESTE',
    'host': 'localhost'

}#diccionario
cone=mysql.connector.connect(**dato)


cursor=cone.cursor()#creando el cursos
valores="insert into usuarios(id, nome, sobrenome, email, senha)  VALUE (DEFAULT ,'alejandro','martinez rivero','amartnezrivero@yahoo.com','alejo2345')"

try:
    cursor.execute(valores)
    cone.commit()
    print("se ha insertado los valores dentro de la base de datos")
except:
    print("no se ha podido insertar los valores en la base de datos")
    cone.close()



