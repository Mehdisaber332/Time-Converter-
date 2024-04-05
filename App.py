from flask import Flask, render_template, request

app = Flask(__name__)

def hours_to_seconds(hours):
    return hours * 3600

def minutes_to_seconds(minutes):
    return minutes * 60

def seconds_to_hours(seconds):
    return seconds / 3600

def seconds_to_minutes(seconds):
    return seconds / 60

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    choice = int(request.form['choice'])
    result = None

    if choice == 1:
        hours = float(request.form['value'])
        result = hours_to_seconds(hours)
    elif choice == 2:
        minutes = float(request.form['value'])
        result = minutes_to_seconds(minutes)
    elif choice == 3:
        seconds = float(request.form['value'])
        result = seconds_to_hours(seconds)
    elif choice == 4:
        seconds = float(request.form['value'])
        result = seconds_to_minutes(seconds)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
