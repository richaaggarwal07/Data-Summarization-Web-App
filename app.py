import requests
from flask import Flask,render_template,url_for
from flask import request as req

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods = ["GET","POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        maxL = int(req.form["maxL"])
        minL = maxL//4
        data = req.form["data"]
        
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })
        return render_template("index.html",result = output[0]['summary_text'])
    else:
        render_template("index.html")    



if __name__ == '__main__':
    app.debug = True
    app.run()
