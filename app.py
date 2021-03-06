from flask import Flask, render_template, redirect, url_for, request, session
from flask_mysqldb import MySQL
app = Flask(__name__)

app.secret_key = "key"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/')
def home():
    return 'Hgwjgolierjgrejhgre'
    
@app.route('/userRegistry',methods=['GET','POST'])
def user_registry():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cur = mysql.connection.cursor()
		cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cur.execute('SELECT * FROM accounts WHERE usename = % s', (username, ))
		account = cur.fetchone()
		if account:
			msg = 'Account already exists'
		else:
			cur.execute('INSERT INTO accounts VALUES (NULL % s, % s, % s)', (username, password,))
		mysql.connection.commit()
		msg= "You have succesfully registered"
	return render_template("userRegistry.html", msg=msg) #render a template
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO App(username, password) VALUES (%s, %s)",(username,password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('login.html')
    
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('welcome'))
    
if __name__== '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)