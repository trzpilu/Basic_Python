from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello"

@app.route('/blog')
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

@app.route('/message_ugly', methods=['GET'])
def message_form_ugly():
    text = """
        <html>
            <head></head>

            <body>
                <form action="" method="POST">
                    <label>First Name</label>
                    <input name="firstname"/>
                    <input type="submit"/>
                </form>
            </body>
        </html  >
    """
    return text
    
@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/warehouse_ugly')
def warehouse_ugly():
    items = ["screwdriver", "hammer", "saw"]
    html = "<ul>"
    for item in items:
        html = html + f"<li>{item}</li>"
    html += "</ul>"
    return html

@app.route('/warehouse')
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    return render_template("warehouse.html", items=items)

@app.route('/add_warehouse')
def add_warehouse():
    items = ["screwdriver", "hammer", "saw"]
    return render_template("add_warehouse.html", items=items)