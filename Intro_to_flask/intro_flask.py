# print('sanity check')

from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'we can change this!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success"


@app.route('/say/<word>/<int:number>')
def say_word(word, number):
    return render_template("say.html", word=word, number=number)


@app.route("/template")
def template():
    new_variable = "this is a test string"
    return render_template("index.html", name_of_variable_on_template = new_variable)

@app.route("/iterate")
def iterate():
    cats = [   
        {
            'name': 'Garfield',
            'color' : 'orange'
        },
        {
            'name': 'Scar',
            'color' : 'dark brown'
        },
        {
            'name': 'Felix',
            'color' : 'black'
        },
    ]
    return render_template("cats.html", cats=cats)


#AWAYS AT THE BOTTOM
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



