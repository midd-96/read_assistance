from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles 
import mysql.connector
# from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# config MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'gokul'
# app.config['MYSQL_DB'] = 'radb'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#init_MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="gokul",
    passwd="gokul123",
    database="radb"
)
cur = mydb.cursor(buffered=True)
#mysql = MySQL(app)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=1,max=50)])
    username = StringField('Username',[validators.length(min=4,max=25)])
    email = StringField('Email',[validators.length(min=6,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message='Passwords do not match')
    ])
    confirm = PasswordField('confirm password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #create_cursor
        #cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        #committ_to_db
        mydb.commit()

        #close_connection
        cur.close()

        flash('you are now registered and log in', 'success')

        redirect(url_for('index'))

        return render_template('register.html', form=form)
    return render_template('register.html', form=form)

if __name__== '__main__':
    app.secret_key='secret123'
    app.run(debug=True)