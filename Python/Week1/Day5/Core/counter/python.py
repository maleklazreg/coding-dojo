from flask import Flask, render_template, redirect, redirect, session  # type: ignore
app = Flask(__name__)
app.secret_key = 'secretker'

@app.route('/')
def visit():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html', visits=session['visits'])

@app.route('/clear')
def destroy_session():
    session['visits'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)