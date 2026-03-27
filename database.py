import sqlite3

def connect_db():
    return sqlite3.connect("history.db", check_same_thread=False)

# Create table
conn = connect_db()
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS history
             (input TEXT, result TEXT)''')
conn.commit()
conn.close()

def save_data(user_input, result):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (?, ?)", (user_input, result))
    conn.commit()
    conn.close()

def get_history():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM history")
    data = c.fetchall()
    conn.close()
    return data