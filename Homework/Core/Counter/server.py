# print("sanity check")

from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key = "secret key"



@app.route('/')
def render_form():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)

    return redirect("/")








if __name__ == "__main__":
    app.run(debug=True)