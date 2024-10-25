from flask import Flask, render_template, request, session, redirect, url_for # type: ignore
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attemps'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['post'])
def guess():
    session['attemps'] += 1
    user_guess = int(request.form ['guess'])

    if user_guess < session['number']:
        feedback = "too low!"
    elif user_guess > session['number']:
        feedback = "too high!"
    else:
        feedback = f"Correct Bro! it took u {session['attemps']} attemps"

    return render_template('index.html', feedback=feedback)

@app.route('/reset')
def reset():
    session.pop('number', None)
    session.pop('attemps', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
