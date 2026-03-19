# address-book-app

An address book application where API users can create, update, delete addresses (CRUD), and retrieve addresses within a given distance using geolocation proximity search.

## Features

- **CRUD Operations**: Create, read, update, and delete addresses
- **Proximity Search**: Find addresses within a specified distance using the Haversine algorithm
- **FastAPI**: RESTful API built with FastAPI framework
- **SQLite Database**: Lightweight database for storing address data
- **Logging**: Comprehensive logging for debugging and monitoring

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory:**
   ```bash
   cd address-book-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt):**
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn requests pydantic
   ```

## Running the Application

### Start the API Server

With the virtual environment activated, run:
```bash
python main.py
```

### Available Endpoints

- `POST /geo-loc/` - Create a new address
- `GET /geo-loc/` - Get all addresses
- `GET /geo-loc/{id}` - Get a specific address by ID
- `GET /geo-loc/nearby?latitude=X&longitude=Y&distance=Z` - Find addresses within a distance
- `PUT /geo-loc/{id}` - Update an address
- `DELETE /geo-loc/{id}` - Delete an address

### Available Endpoints
```python
# Test data payloads
PAYLOAD = {
    "latitude": 35.6762,
    "longitude": 139.6503,
    "address": {
        "street": "1 Chome-1-1 Marunouchi",
        "city": "Tokyo",
        "country": "Japan",
        "zip": "100-6601",
        "landmark": "Tokyo Station"
    }
}

### Interactive API Documentation

Once the server is running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Running Tests

1. **Start the API server** (in one terminal):
   ```bash
   python main.py
   ```

2. **Run the test suite** (in another terminal):
   ```bash
   python test.py
   ```

The tests include:
- Proximity search near Manila (5 km radius)
- Proximity search near New York (10 km radius)
- Small radius search (1 km)
- Invalid distance validation (too small)
- Invalid distance validation (too large)
- Invalid latitude validation

## Project Structure

```
address-book-app/
├── main.py              # FastAPI application and endpoints
├── test.py              # Test suite for the API
├── logger.py            # Logging configuration
├── utils.py             # Utility functions (Haversine distance, validation)
├── model/
│   ├── Address.py       # Pydantic models for address schema
│   └── constants.py     # SQL queries and constants
├── schemas/
│   └── schema.py        # Data schemas
├── logs/
│   └── app.log          # Application logs
└── README.md            # This file
```

## Important Notes

- The database file `geo_address.db` is created automatically on first run
- All locations are stored with latitude/longitude coordinates
- The proximity search uses the Haversine formula for accurate distance calculations
- Valid distance range: 0.1 km to 50,000 km
- Valid latitude range: -90 to 90 degrees
- Valid longitude range: -180 to 180 degrees
