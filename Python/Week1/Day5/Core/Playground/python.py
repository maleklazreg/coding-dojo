from flask import Flask, render_template  # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('index.html', num_boxes=3, color='blue')

@app.route('/play/<int:x>')
def play_with_num(x):
    return render_template('index.html', num_boxes=x, color='blue')

@app.route('/play/<int:x>/<color>')
def play_with_num_and_color(x, color):
    return render_template('index.html', num_boxes=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)