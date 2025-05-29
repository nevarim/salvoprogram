from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return "Admin Section"

@app.route('/board')
def board():
    return "Board Section"

@app.route('/quest')
def quest():
    return "Quest Section"

@app.route('/factions')
def factions():
    return "Factions Section"

@app.route('/media')
def media():
    return "Media Management Section"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)