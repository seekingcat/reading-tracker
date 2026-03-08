from flask import Flask, render_template, redirect, url_for, request
from database import get_all_books, add_book, init_db
init_db()

app = Flask(__name__)

@app.route('/')
def tracker():
    return render_template('tracker.html')

@app.route('/addtitle')
def addtitle_page():
    return render_template('addtitle.html')

@app.route('/view')
def viewtitle():
    books = get_all_books()

    return render_template('viewtitle.html', books = books)


@app.route('/add', methods=['POST'])
def addtitle():
    title = request.form.get('title')
    author = request.form.get('author')
    status = request.form.get('status')

    add_book(title, author, status)
    return redirect(url_for('viewtitle'))


if __name__ == '__main__':
    app.run(debug=True)