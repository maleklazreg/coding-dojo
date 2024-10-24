from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkeredboarddefault():
    rows = 8
    cols = 8
    return render_template('index.html', rows=rows, cols=cols)

@app.route('/<int:cols>')
def checkered_board_x(cols):
    rows = cols
    cols = cols
    return render_template('index.html', rows=rows, cols=cols)

@app.route('/<int:rows>/<int:cols>')
def checkered_board_x_y(rows, cols):
    rows = rows
    cols = cols
    return render_template('index.html', rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)