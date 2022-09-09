from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def render_form():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form['comment']
    return redirect("/result")


@app.route('/result')
def result():
    return render_template("result.html")



if __name__=="__main__":   
    app.run(debug=True) 