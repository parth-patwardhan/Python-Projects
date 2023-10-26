from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def employe():
   
    return render_template('test.html')

@app.route('/result',methods=['POST','GET'])
def user():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "flairminds"
    )
    mycursor=mydb.cursor()
    if request.method == 'POST':
        result = request.form
        name = result['name']
        mycursor.execute("select name1,name2,roll,email from employees where name1='"+name+"'")
        database = mycursor.fetchone()
        print(database)
        mydb.commit()
        mycursor.close()
        return render_template("index.html", database=database)
app.run(debug=True)
