import sqlite3
from logger import logger

# Connect to the database
conn = sqlite3.connect("geo_address.db")
cursor = conn.cursor()

# Query all locations
cursor.execute("SELECT id FROM geo_loc WHERE latitude = ? AND longitude = ?", (35.6762, 139.6503))
rows = cursor.fetchone()

for row in rows:
    logger.info(f"Retrieved row: {row}")