import sqlite3

def addPassword(website, username, password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Drop the table if it exists
    # cursor.execute('DROP TABLE IF EXISTS passwords')

    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT,
            password TEXT,
            username TEXT)
    ''')

    cursor.execute('INSERT INTO passwords (website, password, username) VALUES (?, ?, ?)', (website, password, username))
    conn.commit()
    conn.close()
    print("Password added successfully")
