# print('sanity check')

from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'we can change this!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success"


@app.route('/say/<word>')
def say_word(word):
    return f"the word you gave me is: {word}"

@app.route("/template")
def template():
    return render_template("index.html")


#AWAYS AT THE BOTTOM
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



