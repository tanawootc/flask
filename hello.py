from flask import Flask,render_template,redirect,url_for,request
import pymysql

app=Flask(__name__)
conn=pymysql.connect('localhost','root','root','studentdb')





@app.route("/")
def showdata():
    cur=conn.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    return render_template('index.html',datas=rows)
    
    #age=10
    #return render_template('index.html',data=age)



@app.route("/student")
def showform():
    return render_template('addstudent.html')

@app.route("/insert",methods=['POST'])
def insert():
    if request.method=="POST":
        fname=request.form["fname"]
        lname=request.form["lname"]
        phone=request.form["phone"]
        with conn.cursor() as cursor:
            sql="insert into student(fname,lname,phone) values (%s,%s,%s)"
            cursor.execute(sql,(fname,lname,phone))
            conn.commit()
        return  redirect(url_for('showdata'))


@app.route("/update",methods=['POST'])
def update():
    if request.method=="POST":
        fname=request.form["fname"]
        lname=request.form["lname"]
        phone=request.form["phone"]
        id_update=request.form["id"]
        with conn.cursor() as cursor:
            sql="update student set fname=%s ,lname=%s,phone=%s  where id=%s"
            cursor.execute(sql,(fname,lname,phone,id_update))
            conn.commit()
        return  redirect(url_for('showdata'))

@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn:
        cur=conn.cursor()
        cur.execute("delete from student where id=%s",(id_data))
        conn.commit()
    return  redirect(url_for('showdata'))

            
@app.route("/student2")
def student2():
    return "Student2"

if __name__ == "__main__":
    app.run( debug=True)
    


#https://medium.com/@kongruksiamza/%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A%E0%B9%81%E0%B8%AD%E0%B8%9E%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%8A%E0%B8%B1%E0%B9%88%E0%B8%99%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2-python-python-flask-357c4239092d
