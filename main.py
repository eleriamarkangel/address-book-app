from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import Address
from model.constants import INSERT_GEO_LOC_SQL, GET_ALL_GEO_LOC_SQL, GET_GEO_LOC_BY_ID_SQL, UPDATE_GEO_LOC_SQL, DELETE_GEO_LOC_SQL
from logger import logger
import sqlite3
import json


# FastAPI app
app = FastAPI()

# SQLite database config
DB_NAME = "geo_address.db"

logger.info("Starting address book app")

# CREATE endpoint
@app.post("/geo-loc/")
def create_geo_loc(data: Address):
    # Validate that all fields are present
    if not all([data.latitude, data.longitude, data.address]):
        raise HTTPException(status_code=400, detail="Missing required fields to create: latitude, longitude, address")

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

# READ endpoint (all)
@app.get("/geo-loc/")
def read_all_geo_loc():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(GET_ALL_GEO_LOC_SQL)
        rows = cursor.fetchall()
        
        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "latitude": row[1],
                "longitude": row[2],
                "address": json.loads(row[3])
            })
        
        logger.info(f"Retrieved {len(result)} geo locations")
        return {"total": len(result), "data": result}
    except Exception as e:
        logger.error(f"Server error during geo_loc retrieval: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
    finally:
        conn.close()

# READ endpoint by ID
@app.get("/geo-loc/{geo_loc_id}")
def read_geo_loc(geo_loc_id: int):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(GET_GEO_LOC_BY_ID_SQL, (geo_loc_id,))
        row = cursor.fetchone()
        
        if not row:
            logger.warning(f"Geo location with ID {geo_loc_id} not found")
            raise HTTPException(status_code=404, detail=f"Geo location with ID {geo_loc_id} not found")
        
        result = {
            "id": row[0],
            "latitude": row[1],
            "longitude": row[2],
            "address": json.loads(row[3])
        }
        
        logger.info(f"Retrieved geo location ID: {geo_loc_id}")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Server error during geo_loc retrieval: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
    finally:
        conn.close()

# UPDATE endpoint
@app.put("/geo-loc/{geo_loc_id}")
def update_geo_loc(geo_loc_id: int, data: Address):
    # Validate that all fields are present
    if not all([data.latitude, data.longitude, data.address]):
        raise HTTPException(status_code=400, detail="Missing required fields to update: latitude, longitude, address")
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Check if record exists
        cursor.execute(GET_GEO_LOC_BY_ID_SQL, (geo_loc_id,))
        existing_row = cursor.fetchone()
        
        if not existing_row:
            logger.warning(f"Geo location with ID {geo_loc_id} not found for update")
            raise HTTPException(status_code=404, detail=f"Geo location with ID {geo_loc_id} not found")
        
        # Update the record
        cursor.execute(UPDATE_GEO_LOC_SQL, (data.latitude, data.longitude, json.dumps(data.address), geo_loc_id))
        conn.commit()
        
        logger.info(f"Updated geo location ID: {geo_loc_id}")
        return {"id": geo_loc_id, "latitude": data.latitude, "longitude": data.longitude, "address": data.address}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Server error during geo_loc update: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
    finally:
        conn.close()

# DELETE endpoint
@app.delete("/geo-loc/{geo_loc_id}")
def delete_geo_loc(geo_loc_id: int):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Check if record exists
        cursor.execute(GET_GEO_LOC_BY_ID_SQL, (geo_loc_id,))
        existing_row = cursor.fetchone()
        
        if not existing_row:
            logger.warning(f"Geo location with ID {geo_loc_id} not found for deletion")
            raise HTTPException(status_code=404, detail=f"Geo location with ID {geo_loc_id} not found")
        
        # Delete the record
        cursor.execute(DELETE_GEO_LOC_SQL, (geo_loc_id,))
        conn.commit()
        
        logger.info(f"Deleted geo location ID: {geo_loc_id}")
        return {"message": f"Geo location with ID {geo_loc_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Server error during geo_loc deletion: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
    finally:
        conn.close()