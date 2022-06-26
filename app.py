"""
Este es el controlador. Es como la mente de la app python. Va a ser el encargado de decir: si viene esta URL voy a buscar dat..., si viene esta URL voy a mandarlo esta vista.
Aca se van a hacer todas las redirecciones. Es ocmo la mente de todo.
La vista va a ser el HEML 
"""

from distutils.log import debug
from flask import Flask
from flask import render_template  #Este hace que me lleve a una u otra vista
from flaskext.mysql import MySQL

app=Flask(__name__)  #app va a ser una aplicación del tipo Flask

#esto es toda la configuracion con la base de datos

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'codo_a_codo'
mysql.init_app(app)

@app.route("/")  
def ir_a_index():
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'vale', 'vale@gmail.com', 'fotito2.jpg');" #axa estoy mandando una sentencia sql
    #cuando alguien estra acá quiero abrir una conexión con la base de datos. Entonces:
    conn = mysql.connect() #aca va a tratar de concetarse a la bdd
    #vamos a crear un cursor. es el que va a llevar adentro la sentencia sql
    cursor = conn.cursor() #estoy creando un cursor a partir de la conexion
    cursor.execute(sql)
    conn.commit() #este es el commit de la snetencia sql. eso va y pum! le pega a la BDD, y manda la sentencia que nosotros le dijimos
    return render_template('empleados/index.html')


if __name__ == '__main__': #este es el punto de entrada. Va a correr App: va a ejecutar la aplicacion de Flask.
    app.run(debug=True)