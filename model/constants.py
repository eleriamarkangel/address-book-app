INSERT_GEO_LOC_SQL = """
INSERT INTO geo_loc (latitude, longitude, address) VALUES (?, ?, ?)
"""

GET_ALL_GEO_LOC_SQL = """
SELECT id, latitude, longitude, address FROM geo_loc
"""

GET_GEO_LOC_BY_ID_SQL = """
SELECT id, latitude, longitude, address FROM geo_loc WHERE id = ?
"""

UPDATE_GEO_LOC_SQL = """
UPDATE geo_loc SET latitude = ?, longitude = ?, address = ? WHERE id = ?
"""

DELETE_GEO_LOC_SQL = """
DELETE FROM geo_loc WHERE id = ?
"""

# ===== GLOBAL VARIABLES =====
BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/geo-loc/"