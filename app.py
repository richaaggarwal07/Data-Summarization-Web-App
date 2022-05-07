from flask import Flask,render_template
import requests

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def Index():
    return render_template("index.html")
