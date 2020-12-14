from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello"

@app.route('/contact', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/warehouse')
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    return render_template("warehouse.html", items=items)

