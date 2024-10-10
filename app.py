from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        welcome_message = f"Welcome, {name}! Your date of birth is {dob}."
        return render_template('result.html', message=welcome_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)