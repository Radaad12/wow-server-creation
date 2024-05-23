from flask import Flask, render_template, request, url_for, flash
import mariadb
# ...
app = Flask(__name__)
app.config['SECRET_KEY'] ='aef1f7952234ad5614d387950d15370dd0280c8d92d368f9'

messages = [{'title': 'If Youre Here',
             'content': 'Something Went Wrong'},
            {'title': 'DM',
             'content': 'Rohan Desai, @radaad12'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/register/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        try:
            conn = mariadb.connect(
                user="root",
                password='mangos',
                host = '71.163.107.16',
                port = 3306,
                database = 'test')

            cur= conn.cursor()


            tobehashed= username.upper() + ':' + password.upper()
            print(tobehashed)
    
            QUERY = "INSERT INTO testacct (username,password) VALUES (?, SHA1(?))"

            try: 
                cur.execute(QUERY, (username,tobehashed)) 
            except mariadb.Error as e: 
                return "<p>Error: " +str({e}) + '<p>'
    
            try:
                conn.commit()
                flash("Account Succesfuly Registered. Have Fun")
            except:
                return "Error Inserting"
            conn.close()
        except mariadb.Error as e:
            return "<p>Error connecting to MariaDB Platform: " + str({e}) + '<p>'
        
    return render_template('create.html')