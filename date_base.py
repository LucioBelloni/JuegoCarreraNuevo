import sqlite3

def generar_db():
    with sqlite3.connect("score&name.db") as conexion:
        try:
            sentencia = ''' create  table score
            (
            id integer primary key autoincrement,
            user text,
            score integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla scores&name")
        except sqlite3.OperationalError:
            print("La tabla de scores&name ya existe")

def subir_data(player,score):
    with sqlite3.connect("score&name.db") as conexion:
        try:
            conexion.execute("INSERT INTO score(user,score) VALUES (?,?)", (f"{player}", score))
            conexion.commit()
        except:
            print("Error")

def ordenar_datos():
    with sqlite3.connect("score&name.db") as conexion:
        cursor = conexion.execute("SELECT * FROM score ORDER BY score DESC;")
        lista_scores = []
    for fila in cursor:
        lista_scores.append(fila)
    return lista_scores