from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello"

@app.route('/Dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:number>/<string:word>')
def repeat_word(number, word):
    return (word + " ") * number

@app.errorhandler(404)
def not_found(e):
    return "Sorry, the page you are looking for could not be found." , 404
 
if __name__ == "__main__":
    app.run(debug=True)