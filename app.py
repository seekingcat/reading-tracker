from flask import Flask, render_template, redirect, url_for, request
from database import get_all_books, add_book, init_db, delete_book, get_books_by_status, update_book_status
init_db()

app = Flask(__name__)

@app.route('/')
def tracker():
    return render_template('tracker.html')

@app.route('/addtitle')
def addtitle_page():
    return render_template('addtitle.html')

@app.route('/view/<status>')
def viewbystatus(status):
    books = get_books_by_status(status)
    return render_template('viewtitle.html', books = books, current_status = status)



@app.route('/view')
def viewtitle():
    books = get_all_books()

    return render_template('viewtitle.html', books = books, current_status = 'all')


@app.route('/add', methods=['POST'])
def addtitle():
    title = request.form.get('title')
    author = request.form.get('author')
    status = request.form.get('status')

    add_book(title, author, status)
    return redirect(url_for('viewtitle'))

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book_route(book_id):
    if request.method == 'POST':
        # Handle the form submission
        new_status = request.form.get('status')
        update_book_status(book_id, new_status)
        return redirect(url_for('viewtitle'))
    else:
        # Show the edit form
        books = get_all_books()
        book = next((b for b in books if b['id'] == book_id), None)
        
        if not book:
            return "Book not found", 404
        
        return render_template('edittitle.html', book=book)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book_route(book_id):
    delete_book(book_id)
    return redirect(url_for('viewtitle'))


if __name__ == '__main__':
    app.run(debug=True)