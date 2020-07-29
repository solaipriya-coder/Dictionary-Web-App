from flask import Flask, render_template, request
import wikipedia
app = Flask(__name__)
app.config["DEBUG"]=True
@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')


@app.route("/answer", methods=["GET", "POST"])
def answer():
    if request.method == "POST":
        word = None
        num = None
        word = request.form["word"]
        num = int(request.form["num"])
        if word is not None and num is not None:
            result= wikipedia.summary(word,sentences=num)
        return '''
                <html>
                    <body>
                        <p> {result}</p>
                       
                    </body>
                </html>
            '''.format(result=result)
if __name__ =="__main__":
    app.run()