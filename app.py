from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key="abc"

con=sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS data(pid INTEGER PRIMARY KEY, name TEXT,address TEXT, contact INTEGER, mail TEXT)")
con.close()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_record')
def add_record():
    return render_template('add_record.html')

@app.route('/addData',methods=["POST","GET"])
def addData():
    if request.method=='POST':
        try:
            name=request.form['name']
            address=request.form['address']
            contact=request.form['contact']
            mail=request.form['mail']
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("INSERT INTO data(name,address,contact,mail)values(?,?,?,?)",(name,address,contact,mail))
            con.commit()
            flash("Record Added Successfully","success")
        except:
            flash("Error in Insert Operation", "danger")
        finally:
            return redirect(url_for("home"))        
            con.close()
if __name__ == '__main__':
    app.run(debug=True)