from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

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
    #abort(450)
    #return redirect(url_for('post', post_id=2))
    # print(request.form)
    # print(request.form['key1'])
    # print(request.form['key2'])
    #return render_template('dummy.html')
    return {
        "username": 'Chanchito Feliz',
        "email": 'chanchito@feliz.com'
    }


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', message='Hello World')