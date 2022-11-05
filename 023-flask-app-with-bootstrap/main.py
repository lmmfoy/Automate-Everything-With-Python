from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Note, Flask will look in templates folder automatically
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def home_post(): 
    dim1 = request.form["first_dim"]
    dim2 = request.form["second_dim"]
    dim3 = request.form["third_dim"]

    volume = float(dim1) * float(dim2) * float(dim3)
    return render_template("index.html", output=volume, dim1=dim1, dim2=dim2, dim3=dim3)

app.run()