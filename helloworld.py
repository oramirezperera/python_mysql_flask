from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin',
    database = 'pruebaudemy'
)

cursor = mydb.cursor(dictionary=True)

app = Flask(__name__) #entry point of the program

@app.route('/') # this is the route from te web browser
def index():
    return 'hello world'

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    return 'el id del post es ' + post_id

@app.route('/lolo', methods=['POST', 'GET'])
def lolo():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    #abort(450)
    #return redirect(url_for('post', post_id=2))
    # print(request.form)
    # print(request.form['key1'])
    # print(request.form['key2'])
    #return render_template('dummy.html')
    # return {
    #     "username": 'Chanchito Feliz',
    #     "email": 'chanchito@feliz.com'
    # }
    return render_template('dummy.html', usuarios=usuarios)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', message='Hola Milipza')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = 'insert into usuario (username, email, edad) values (%s, %s, %s)'
        values = (username, email, edad)
        cursor.execute(sql, values)
        mydb.commit()

        return redirect(url_for('lolo'))
    return render_template('create.html')