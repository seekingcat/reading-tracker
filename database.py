import sqlite3
from datetime import datetime

def get_db():
    conn = sqlite3.connect('book.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT,
            added_at TEXT NOT NULL
        )  
    ''')

    conn.commit()
    conn.close()


def get_all_books():
    conn = get_db()
    cursor = conn.cursor()

    books = cursor.execute('SELECT * FROM book').fetchall()

    result = []
    for book in books:
        result.append({
            'id': book['book_id'],
            'title': book['title'],
            'author': book['author'],
            'status': book['status']
        })

    conn.close()
    return result


def add_book(title, author, status):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO book (title, author, status, added_at) VALUES (?, ?, ?, ?)',
        (title, author, status, datetime.now().date().isoformat())
    )

    conn.commit()
    conn.close()

def get_books_by_status(status):
    conn = get_db()
    cursor = conn.cursor()

    books = cursor.execute('SELECT * FROM book where status = ?', (status,)).fetchall()

    result = []
    for book in books:
        result.append({
            'id': book['book_id'],
            'title': book['title'],
            'author': book['author'],
            'status': book['status']
        })

    conn.close()
    return result

def delete_book(book_id):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM book WHERE book_id = ?', (book_id,))
    
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    init_db()
    print("Database created!")