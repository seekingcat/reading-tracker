import sqlite3

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

if __name__ == '__main__':
    init_db()
    print("Database created!")