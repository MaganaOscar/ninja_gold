from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = b'\xa7\xff\xcf\xd6\xafp\x8a6\xd3\xfd\x03<h\xcb\xf0c'
@app.route('/')
def index():
    if 'moves' not in session:
        session['moves'] = 0
    else:
        session['moves'] += 1
    if 'activities' not in session:
        session['activities'] = []
    if 'gold' not in session:
        session['gold'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    building = request.form['building']
    if building == 'farm':
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        earned = random.randint(10,20)
        session['gold'] += earned
        session['activities'].append("<div class='text-success'>Earned " + str(earned) + " gold from the farm! (" + nowString + ")</div>")
    elif building == 'cave':
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        earned = random.randint(5,10)
        session['gold'] += earned
        session['activities'].append("<div class='text-success'>Earned " + str(earned) + " gold from the cave! (" + nowString + ")</div>")
    elif building == 'house':
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        earned = random.randint(2,5)
        session['gold'] += earned
        session['activities'].append("<div class='text-success'>Earned " + str(earned) + " gold from the house! (" + nowString + ")</div>")
    elif building == 'casino':
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        earned = random.randint(-50,50)
        session['gold'] += earned
        if earned > 0:
            session['activities'].append("<div class='text-success'>Earned " + str(earned) + " gold from the casino! (" + nowString + ")</div>")
        else:
            session['activities'].append("<div class='text-danger'>Entered a casino and lost " + str(earned) + " gold... Ouch! (" + nowString + ")</div>")
    print(session['activities'])
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)