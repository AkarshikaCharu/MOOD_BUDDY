import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = 'mood_buddy.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    c.execute('''CREATE TABLE IF NOT EXISTS chats 
                 (username TEXT, role TEXT, message TEXT, mood_score REAL, timestamp TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO users(username, password) VALUES (?,?)', (username, password))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username =? AND password =?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

def save_message(username, role, message, score=0.0):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO chats(username, role, message, mood_score, timestamp) VALUES (?,?,?,?,?)',
              (username, role, message, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_chat_history(username):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql(f"SELECT role, message, mood_score, timestamp FROM chats WHERE username='{username}' ORDER BY timestamp ASC", conn)
    conn.close()
    return df