from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/mentor')
def mentor():
    return render_template('mentor.html')

@app.route('/secretflag')
def segredosupersecreto():
    return render_template('flag.html')

if __name__ == '__main__':
    app.run(debug=False)