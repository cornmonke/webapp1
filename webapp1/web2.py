from flask import Flask, render_template, redirect, session, url_for, request
from datetime import timedelta


app = Flask(__name__)
app.secret_key="y4resdckuyorutycghnblj5"
app.permanent_session_lifetime = timedelta(days=1)
pagenum=1
rating=None
login=False


@app.route('/')
def index():
    global pagenum
    pagenum=1
    return redirect(url_for('home'))

@app.route('/home')
def home():
    global pagenum
    match pagenum:
        case 1:
            return render_template('home/home.html')
        case 2:
            return render_template('home/monkey.html')
        case 3:
            return render_template('home/laptop.html')
        case 4:
            return render_template('home/desktop.html')
        case 5:
            return render_template('home/photos.html')
        case 6:
            return render_template('home/earbuds.html')
        case 7:
            return render_template('home/planner.html')
        case 8:
            return render_template('home/watch.html')
        case 9:
            return render_template('home/lego.html')
        case 10:
            return render_template('home/ball.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/monkey')
def monkey():
    global pagenum
    pagenum=2
    return redirect(url_for('home'))

@app.route('/laptop')
def laptop():
    global pagenum
    pagenum=3
    return redirect(url_for('home'))

@app.route('/desktop')
def desktop():
    global pagenum
    pagenum=4
    return redirect(url_for('home'))

@app.route('/photos')
def photos():
    global pagenum
    pagenum=5
    return redirect(url_for('home'))

@app.route('/earbuds')
def earbuds():
    global pagenum
    pagenum=6
    return redirect(url_for('home'))

@app.route('/planner')
def planner():
    global pagenum
    pagenum=7
    return redirect(url_for('home'))

@app.route('/watch')
def watch():
    global pagenum
    pagenum=8
    return redirect(url_for('home'))

@app.route('/lego')
def lego():
    global pagenum
    pagenum=9
    return redirect(url_for('home'))

@app.route('/ball')
def ball():
    global pagenum
    pagenum=10
    return redirect(url_for('home'))

@app.route('/review', methods=['POST','GET'])
def review():
    global rating
    if rating != None:
        return render_template('submitted.html', name=session["name"])
    if request.method =="POST":
        rating=request.form["rating"]
        name=request.form["name"]
        if name=="":
            name="Anonymous"
        session["name"]= name
        session["rating"]= rating
        return render_template('submitted.html', name=name)
    elif request.method =="GET":
        return render_template('review.html')

@app.route('/admin', methods=['POST','GET'])
def admin():
    attempts = session.get("attempts", 3)
    global login
    if attempts<=0:
        return render_template('login.html', fail=True, attempts=attempts)
    if request.method =="POST":
        if attempts<=0:
            redirect(url_for("home"))
        elif request.form["name"]=="admin" and request.form["pwd"]=="admin":
            login=True
            return render_template('admin.html')
        else:
            attempts-=1
            session["attempts"]=attempts
            return render_template('login.html', fail=True, attempts=attempts)
    elif request.method =="GET":
        return render_template('login.html',fail=False,attempts=attempts)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
