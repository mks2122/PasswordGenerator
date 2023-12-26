import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

# Drop the table if it exists
# cursor.execute('DROP TABLE IF EXISTS passwords')
def addPassword(website, password, username):
    
    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT,
            password TEXT,
            username TEXT)
    ''')

    cursor.execute('INSERT INTO passwords (website, password, username) VALUES (?, ?, ?)', (website, password, username))




# Insert records into the table

# Commit the changes and close the database connection
conn.commit()
conn.close()


