from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import Address
from model.constants import INSERT_GEO_LOC_SQL
from logger import logger
import sqlite3
import json


# FastAPI app
app = FastAPI()

# SQLite database config
DB_NAME = "geo_address.db"

# CREATE endpoint
@app.post("/geo-loc/")
def create_geo_loc(data: Address):
    # Validate that all fields are present
    if not all([data.latitude, data.longitude, data.address]):
        raise HTTPException(status_code=400, detail="Missing required fields: latitude, longitude, address")

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(INSERT_GEO_LOC_SQL, (data.latitude, data.longitude, json.dumps(data.address)))
        conn.commit()
        new_id = cursor.lastrowid
        return {"id": new_id, "latitude": data.latitude, "longitude": data.longitude, "address": data.address}
    except sqlite3.IntegrityError as e:
        # Specific database constraint errors
        logger.error(f"Database integrity error: {e}")
        raise HTTPException(status_code=400, detail=f"Integrity error: {e}")
    except Exception as e:
        # Any other error
        logger.error(f"Server error during geo_loc creation: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
    finally:
        conn.close()