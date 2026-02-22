from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def tracker():
    return render_template('tracker.html')

@app.route('/add')
def addtitle():
    return render_template('addtitle.html')

if __name__ == '__main__':
    app.run(debug=True)