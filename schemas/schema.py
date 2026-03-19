import sqlite3

# NOTE!!! Can only be executed once to create the database and table.
# Connect (or create) a database file
conn = sqlite3.connect("geo_address.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS geo_loc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    address JSON
)
""")

# Commit changes and close
conn.commit()
conn.close()