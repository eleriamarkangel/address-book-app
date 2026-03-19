INSERT_GEO_LOC_SQL = """
INSERT INTO geo_loc (latitude, longitude, address) VALUES (?, ?, ?)
"""

GET_ALL_GEO_LOC_SQL = """
SELECT id, latitude, longitude, address FROM geo_loc
"""

GET_GEO_LOC_BY_ID_SQL = """
SELECT id, latitude, longitude, address FROM geo_loc WHERE id = ?
"""