from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def employee():
    return render_template('website.html')

@app.route('/create',methods=['POST','GET'])
def users():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "flairminds"
    )
    mycursor = mydb.cursor()



    if request.method=='POST':
        
        result=request.form.to_dict()
        fname = result['name']
        lname = result['lname']
        rollno = result['roll_no']
        mail_id = result['mail_id']
        mycursor.execute("insert into employees (name1,name2,roll,email) values(%s,%s,%s,%s)",(fname,lname,rollno,mail_id))
        mydb.commit()
        mycursor.close()
        return render_template('store.html',result=result)
        
    return render_template('website.html')
        
app.run(debug=True)