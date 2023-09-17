import sqlite3

def create_database():
    conn = sqlite3.connect('360_feedback.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS news_articles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 content TEXT,
                 website TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS video_transcripts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 video_path TEXT,
                 transcript TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS news_clippings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 clipping_path TEXT,
                 newspaper_name TEXT,
                 page_number INTEGER,
                 edition TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS categorized_news_clippings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 clipping_id INTEGER,
                 department TEXT,
                 tonality TEXT)''')

    # Save changes and close connection
    conn.commit()
    conn.close()

def insert_news_article(title, content, website):
    conn = sqlite3.connect('360_feedback.db')
    c = conn.cursor()

    c.execute("INSERT INTO news_articles (title, content, website) VALUES (?, ?, ?)",
              (title, content, website))

    # Save changes and close connection
    conn.commit()
    conn.close()

def insert_video_transcript(video_path, transcript):
    conn = sqlite3.connect('360_feedback.db')
    c = conn.cursor()

    c.execute("INSERT INTO video_transcripts (video_path, transcript) VALUES (?, ?)",
              (video_path, transcript))

    # Save changes and close connection
    conn.commit()
    conn.close()

def insert_news_clipping(clipping_path, newspaper_name, page_number, edition):
    conn = sqlite3.connect('360_feedback.db')
    c = conn.cursor()

    c.execute("INSERT INTO news_clippings (clipping_path, newspaper_name, page_number, edition) VALUES (?, ?, ?, ?)",
              (clipping_path, newspaper_name, page_number, edition))

    # Save changes and close connection
    conn.commit()
    conn.close()

def insert_categorized_news_clipping(clipping_id, department, tonality):
    conn = sqlite3.connect('360_feedback.db')
    c = conn.cursor()

    c.execute("INSERT INTO categorized_news_clippings (clipping_id, department, tonality) VALUES (?, ?, ?)",
              (clipping_id, department, tonality))

    # Save changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
