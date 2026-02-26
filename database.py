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
            synopsis TEXT,
            review TEXT
            added_at TEXT NOT NULL
        )  
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS author (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            publisher TEXT,
            country TEXT
        )  
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database created!")