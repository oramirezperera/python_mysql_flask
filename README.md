# python_mysql_flask
learning flask, and combining python with mysql

## db.py mysql-connector
using the [mysql.connector](https://dev.mysql.com/doc/connector-python/en/) 
installed by pip install mysql-connector-python

with this library you can use python to do full CRUD changes to a mysql database
inside the db.py file there are all the CRUD syntax and the configuration to make the connection to the server.

## Flask

You have to export the flask app, to do that type export FLASK_APP='name file' (set in windows)
with that done you can run your app by typing flask run

flask don't update the files constantly, but you can configurate a development environment where you can easily add new files

to do this we shut down the running flask server and then type export FLASK_ENV=development


### variables in urls

You can pass variables directly from the web browser url in flask. 
The variable will always be a string, but you can change this by writing <\int:variable_name>

### HTTP methods in flask

managing four HTTP methods, GET, POST, PUT and DELETE.

GET lets you show data.
POST allows you to create.
PUT allows you to update.
DELETE for delete.

There is a PATCH method, and works similarly to PUT but instead of changing a value, allows you to partially update a resource. 

You can use the post method in the terminal using the curl command.
curl -x [method] http://localhost:5000/post/1
curl is used to transfer data from or to a server, admit several protocols, like HTTP and TELNET.
-x lets you use a proxy to access the URL
method in this moment can be GET or POST.

The logic of the methods can be separated by methods, so each function manage a different method.

with request (request needs to be imported from flask) I can access to the method that is being called using: 
    if request.method == 'GET':
        do something
    else:
        do something else

### Data from a form

you can handle data from a webclient in your flask server, and with flask take actions with that data.
you have to build a complete form to do this or you can use curl(for educational purposes we will be using curl, but, we will use forms later)

curl works for making calls to servers and APIs.

with curl -d you can send data
curl -d "key1=data1&key2=data2" -X (method) url

### building URLs

By building URLs you can redirect the user to a predefined path.
For this we need to import url_for.
In url_for() you pass the function that you want to use, not the url, the function.
If you are passing a function that needs an argument, you have to inline define the argument like for example post_id=2 


### Redirecting the user

We need to import redirect function from flask.
To use redirect I'm going to change the print function to redirect.
ALWAYS you have to return the redirect function. 

### Handling errors and aborts

You have to import abort from flask.
With abort, you can stop your program and send a message to the user. If you use the number of the error they will be printed as a message to the user.
The message will be in plain HTML, but capturing the error you can change and present a different page with more detailed text or something you want to share with your user.

### Rendering forms

To the user we want to show them jsons or html pages.
To do this we can use render_template('web.html').
import render_template
When you use render_template, flask is going to search a folder called template and in there is going to search for a file called web.html.

### Returning Json

You have to return a dictionary and define what do you want to show.
Returning Jsons is good when you are working with APIs.

### More templates

When you use render_template('home.html', ) you can render variables too.
to pass that variable in HTML use {{ variable_name }} 
You can reuse some things like headers and footers, to do this we are going to create a new file called base.html.
With this syntax {% block title %}{% endblock %} you have will have a parent or base html, and you can reference with this son you can change the title or re use it with other values. You can always change the values of these tags.
Another thing is in this syntax href="{{ url_for('static', filename='style.css') }}" you can render Python code, in the first argument you have static, that is a folder that has css files, and the second argument is the name of the css file that we want to use.

The home file will be the son, in the son we use {% extends 'base.html' %} {% block content %} {% endblock %}, with this syntax we are using the references from the parent file.

### Import data from database

Using the syntax {% for usuario in usuarios %} this will start a Python for loop in our HTML file, to end this script you will need to write {% endfor %}.
In cursor you can pass the argument dictionary = True, with this they are sorted by the name because the return will not be a tuple instead will be a dictionary.
With the dictionary=True, you can now use the for loop with usuario.username, to iterate over the usernames and print them. You can use syntax [\'\username'] too.

### Insert data to the database

It's important the name that you declare in the HTML input, because that's the name you will use in Python.