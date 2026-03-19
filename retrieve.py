import sqlite3
from logger import logger

# Connect to the database
conn = sqlite3.connect("geo_address.db")
cursor = conn.cursor()

# Query all locations
cursor.execute("SELECT * FROM geo_loc")
rows = cursor.fetchall()

for row in rows:
    logger.info(f"Retrieved row: {row}")

conn.close()