from flask import Flask, render_template, redirect, url_for
from database import get_all_books, add_book, init_db
init_db()

app = Flask(__name__)

@app.route('/')
def tracker():
    return render_template('tracker.html')

@app.route('/add')
def addtitle():
    return render_template('addtitle.html')

@app.route('/view')
def viewtitle():
    books = get_all_books()

    return render_template('viewtitle.html', books = books)

if __name__ == '__main__':
    app.run(debug=True)