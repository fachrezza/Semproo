from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/congrats')
def congrats():
    return render_template('congrats.html')

@app.route('/wrong')
def goodbye():
    return render_template('wrong.html')

if __name__ == '__main__':
    app.run(debug=True)
