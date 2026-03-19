import sqlite3

# Connect (or create) a database file
conn = sqlite3.connect("address_book.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS geoloc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    label TEXT
)
""")

# Commit changes and close
conn.commit()
conn.close()