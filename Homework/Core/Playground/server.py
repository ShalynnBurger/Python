# print("sanity check")

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html",  color='rgb(16,253,254) ', number= 3)

@app.route('/play/<int:number>')
def printNumber(number):
    return render_template("index.html" ,color='rgb(16,253,254)', number= number)

@app.route('/play/<int:number>/<color>')
def ColorNumber(number,color):
    return render_template("index.html" ,color=color, number=number)

if __name__=="__main__":
    app.run(debug=True)