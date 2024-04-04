# from flask import Flask, render_template, request, redirect, url_for, session
# import mysql.connector

# app = Flask(__name__)

# db = mysql.connector.connect(
#     host='localhost',
#     username='root',
#     password='manikandan22072003',
#     database='mani')

# cursor = db.cursor()
# @app.route('/')
# def intro():
#        return render_template("index.html")

# @app.route('/staff_create',methods=['GET','POST'])
# def staff_create():
#     return render_template("create_exam.html")


# @app.route('/staff',methods=['GET','POST'])
# def staff():
#      if request.method == 'POST':
#        # userid = request.form['userid']
#         username = request.form['username']
#         password = request.form['password']
#         check_query="SELECT * FROM exam_controller WHERE username = %s AND password=%s  "
#         values=(username,password)
#         cursor.execute(check_query,values)
#         allow = cursor.fetchone()

#         if allow:
#             return redirect(url_for('staff_create'))
            
#         else:
#             return render_template('staff_login.html', error_msg='Invalid username or password')

#      return render_template('staff_registration.html', error_msg=None)
        





# @app.route('/staff_registration', methods=['GET','POST'])
# def staff_registration():
#     error_statement = None
#     if request.method == 'POST':
#         userid=request.form['userid']
#         username = request.form['username']
#         password = request.form['password']
#         check_query = "SELECT * FROM exam_controller WHERE username = %s"
#         cursor.execute(check_query, (username,))
#         exist_student = cursor.fetchone()

#         if exist_student:
#             error_statement = "Entry with " + username + " username is already Exist"
#         else:
#             query = "INSERT INTO exam_controller(userid ,username, password) VALUES (%s, %s, %s)"
#             values = (userid,username, password)
#             cursor.execute(query, values)
#             db.commit()
#             return render_template("staff_login.html")
#     return render_template("staff_registration.html", error_msg=error_statement)   

# @app.route('/student_login')
# def student_login():
#      return render_template('studentlogin.html')

# @app.route('/studentindex')   
# def studentindex():
#     return render_template("student_index.html")

# @app.route('/student_reg',methods=['GET','POST'])
# def student_reg():
#     return render_template("student_register.html")

# @app.route('/staff_reg',methods=['GET','POST'])
# def staff_reg():
#     return render_template("staff_registration.html")    



# @app.route('/staff_log',methods=['GET','POST'])
# def staff_log():
#     return render_template("staff_login.html")   
 
# @app.route('/student_home', methods=['GET', 'POST'])
# def student_home():
#     # Here, you need to fetch the user's name from the database
#     # Assuming you have the username stored in session after login
#     username = request.args.get('username')

#     # Assuming you have a query to get the user's name based on their username
#     query = "SELECT username FROM students_details WHERE username = %s"
#     cursor.execute(query, (username,))
#     user_data = cursor.fetchone()
#     if user_data:
#         user_name = user_data[0]
#     else:
#         user_name = "Guest"  # If user data not found, you can set a default name

#     return render_template("student_home.html", user_name=user_name)


# @app.route('/exam_register', methods=['GET','POST'])
# def exam_register():
#     if request.method == 'POST':
#         error_statement=None
#         f=0
#         name=request.form['exam_name']
#         code=request.form['code']
#         description=request.form['description']
#         amount=request.form['amount']
#         check_query = "SELECT * FROM exam WHERE code = %s"
#         cursor.execute(check_query, (code,))
#         exist_exam = cursor.fetchone()

#         if exist_exam:
#             error_statement = "Entry with " + code + " code is already Exist"
#         else:
#             query = "INSERT INTO exam(name ,code, description, amount) VALUES (%s, %s, %s, %s)"
#             values = (name, code, description, amount)
#             cursor.execute(query, values)
#             db.commit()
#             return render_template("create_exam.html")
#         return render_template("staff_login.html", error_msg=error_statement)

# @app.route('/student_exam_reg', methods=['GET','POST'])
# def student_exam_reg():
#     return render_template("payment.html")

# @app.route('/student_exam_register',methods=['GET','POST'])
# def student_exam_register():
#     if request.method == 'POST':
#         pass
    
#     # Fetch exams from the database
#     cursor.execute("SELECT * FROM exam")
#     exam = cursor.fetchall()
    
#     # Render the template with exams data
#     return render_template("student_exam.html",exams=exam)
            

# @app.route('/student_register', methods=['GET', 'POST'])
# def student_register():
#     if request.method == 'POST':
#         # Get form data
#         f=0
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         # Insert data into the database
#         insert_query = "INSERT INTO students_details (username, email, password) VALUES (%s, %s, %s)"
#         values = (username, email, password, )
#         f=cursor.execute(insert_query, values)
#         db.commit()
        
#         if f:
#             return render_template('studentlogin.html')
#     return render_template('student_register.html') 

# @app.route('/student_log', methods=['GET','POST'])
# def student_log():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         check_query="SELECT * FROM students_details WHERE username = %s AND password=%s"
#         values=(username,password)
#         cursor.execute(check_query,values)
#         allow = cursor.fetchone()

#         if allow:
#             return redirect(url_for('student_home'))
#         else:
#             return render_template('studentlogin.html', error_msg='Invalid username or password')

#     return render_template('studentlogin.html', error_msg=None)



# if __name__=="__main__":

#     cursor.execute('''CREATE TABLE IF NOT EXISTS students_details (
#   id INT NOT NULL AUTO_INCREMENT,
#   username VARCHAR(45) NOT NULL,
#   email VARCHAR(45) NOT NULL,
#   password VARCHAR(45) NOT NULL,
#   regexam VARCHAR(45) NULL,
#   PRIMARY KEY (`id`)
#         )
#     ''')
#     cursor.execute('''CREATE TABLE IF NOT EXISTS exam_controller (
#             userid INT NOT NULL UNIQUE ,
#             username VARCHAR(20) NOT NULL UNIQUE,
#             passcode VARCHAR(20) NOT NULL UNIQUE
#         )
#     ''')


#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

# Set a secret key for sessions to work securely
app.secret_key = 'your_secret_key_here'

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='manikandan22072003',
    database='mani')

cursor = db.cursor()

@app.route('/')
def intro():
    return render_template("index.html")

@app.route('/staff_create', methods=['GET', 'POST'])
def staff_create():
    return render_template("create_exam.html")

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        check_query = "SELECT * FROM exam_controller WHERE username = %s AND password = %s"
        cursor.execute(check_query, (username, password))
        allow = cursor.fetchone()

        if allow:
            # Store user data in session
            session['username'] = username
            return redirect(url_for('staff_create'))
        else:
            return render_template('staff_login.html', error_msg='Invalid username or password')

    return render_template('staff_registration.html', error_msg=None)

@app.route('/staff_registration', methods=['GET', 'POST'])
def staff_registration():
    error_statement = None
    if request.method == 'POST':
        userid = request.form['userid']
        username = request.form['username']
        password = request.form['password']
        check_query = "SELECT * FROM exam_controller WHERE username = %s"
        cursor.execute(check_query, (username,))
        exist_student = cursor.fetchone()

        if exist_student:
            error_statement = "Entry with " + username + " username is already Exist"
        else:
            query = "INSERT INTO exam_controller(userid ,username, passcode) VALUES (%s, %s, %s)"
            values = (userid, username, password)
            cursor.execute(query, values)
            db.commit()
            return render_template("staff_login.html")
    return render_template("staff_registration.html", error_msg=error_statement)

@app.route('/student_login')
def student_login():
    return render_template('studentlogin.html')

@app.route('/studentindex')
def studentindex():
    return render_template("student_index.html")

@app.route('/student_reg', methods=['GET', 'POST'])
def student_reg():
    return render_template("student_register.html")

@app.route('/staff_reg', methods=['GET', 'POST'])
def staff_reg():
    return render_template("staff_registration.html")

@app.route('/staff_log', methods=['GET', 'POST'])
def staff_log():
    return render_template("staff_login.html")

@app.route('/student_home', methods=['GET', 'POST'])
def student_home():
    # Retrieve username from session
    username = session.get('username')

    # Assuming you have a query to get the user's name based on their username
    query = "SELECT username FROM students_details WHERE username = %s"
    cursor.execute(query, (username,))
    user_data = cursor.fetchone()
    if user_data:
        user_name = user_data[0]
    else:
        user_name = "Guest"  # If user data not found, set a default name

    return render_template("student_home.html", user_name=user_name)

@app.route('/exam_register', methods=['GET', 'POST'])
def exam_register():
    if request.method == 'POST':
        error_statement = None
        name = request.form['exam_name']
        code = request.form['code']
        description = request.form['description']
        amount = request.form['amount']
        check_query = "SELECT * FROM exam WHERE code = %s"
        cursor.execute(check_query, (code,))
        exist_exam = cursor.fetchone()

        if exist_exam:
            error_statement = "Entry with " + code + " code is already Exist"
        else:
            query = "INSERT INTO exam(name ,code, description, amount) VALUES (%s, %s, %s, %s)"
            values = (name, code, description, amount)
            cursor.execute(query, values)
            db.commit()
            return render_template("create_exam.html")
        return render_template("staff_login.html", error_msg=error_statement)

@app.route('/student_exam_reg', methods=['GET', 'POST'])
def student_exam_reg():
    username = session.get('username')
    code=request.form['code']
    name=request.form['name']

    # Assuming you have a query to get the user's name based on their username
    query = "SELECT username FROM students_details WHERE username = %s"
    cursor.execute(query, (username,))
    user_data = cursor.fetchone()
    if user_data:
        user_name = user_data[0]
        sqlquery="INSERT INTO exam_registered_1 (name, exam_name,code ) VALUES(%s,%s,%s)"
        values = (username, name, code)
        cursor.execute(sqlquery, values)
        db.commit()
        
    else:
        user_name = "Guest"  # If user data not found, set a default name

    return render_template("student_home.html", user_name=user_name)

@app.route('/student_view_exam',methods=['GET','POST'])
def student_view_exam():
    username = session.get('username')
    query="SELECT * from exam_registered_1 where name=%s"
    cursor.execute(query,(username,))
    exams=cursor.fetchall()
    return render_template("view_exam.html",exams=exams)

    

@app.route('/student_exam_register', methods=['GET', 'POST'])
def student_exam_register():
    if request.method == 'POST':
        pass

    # Fetch exams from the database
    cursor.execute("SELECT * FROM exam")
    exam = cursor.fetchall()

    # Render the template with exams data
    return render_template("student_exam.html", exams=exam)

@app.route('/student_register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Insert data into the database
        insert_query = "INSERT INTO students_details (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)
        cursor.execute(insert_query, values)
        db.commit()

        # Store username in session
        session['username'] = username

        return render_template('studentlogin.html')

    return render_template('student_register.html')

@app.route('/student_log', methods=['GET', 'POST'])
def student_log():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        check_query = "SELECT * FROM students_details WHERE username = %s AND password=%s"
        cursor.execute(check_query, (username, password))
        allow = cursor.fetchone()

        if allow:
            # Store username in session
            session['username'] = username
            return redirect(url_for('student_home'))
        else:
            return render_template('studentlogin.html', error_msg='Invalid username or password')

    return render_template('studentlogin.html', error_msg=None)

if __name__ == "__main__":
    cursor.execute('''CREATE TABLE IF NOT EXISTS students_details (
      id INT NOT NULL AUTO_INCREMENT,
      username VARCHAR(45) NOT NULL,
      email VARCHAR(45) NOT NULL,
      password VARCHAR(45) NOT NULL,
      regexam VARCHAR(45) NULL,
      PRIMARY KEY (`id`)
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS exam_controller (
        userid INT NOT NULL UNIQUE ,
        username VARCHAR(20) NOT NULL UNIQUE,
        passcode VARCHAR(20) NOT NULL UNIQUE
    )''')

    app.run(debug=True)


