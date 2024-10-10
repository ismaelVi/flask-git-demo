from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        age = calculate_age(dob)
        welcome_message = f"Welcome, {name}! You are {age} years old."
        return render_template('result.html', message=welcome_message)
    return render_template('index.html')
                           

def calculate_age(dob):
    today = datetime.today()
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


if __name__ == '__main__':
    app.run(debug=True)