import requests
import json
from logger import logger

# ===== GLOBAL VARIABLES =====
BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/geo-loc/"

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

PAYLOAD_UPDATED = {
    "latitude": 14.6020,
    "longitude": 120.9850,
    "address": {
      "street": "San Miguel Avenue",
      "city": "Manila",
      "country": "Philippines",
      "landmark": "San Miguel Parish Church"
    }
}

# CRUD Operations
CRUD_CREATE = "C"
CRUD_READ = "R"
CRUD_UPDATE = "U"
CRUD_DELETE = "D"

# ===== HELPER FUNCTIONS =====
def build_url(action, resource_id=None):
    """Build URL based on CRUD action"""
    base = f"{BASE_URL}{ENDPOINT}"
    if action == CRUD_READ and resource_id:
        return f"{base}{resource_id}"
    elif action == CRUD_UPDATE and resource_id:
        return f"{base}{resource_id}"
    elif action == CRUD_DELETE and resource_id:
        return f"{base}{resource_id}"
    return base

def get_http_method(action):
    """Get HTTP method based on CRUD action"""
    methods = {
        CRUD_CREATE: "POST",
        CRUD_READ: "GET",
        CRUD_UPDATE: "PUT",
        CRUD_DELETE: "DELETE"
    }
    return methods.get(action, "GET")

# ===== MAIN TEST FUNCTION =====
def test_crud(action, payload=None, resource_id=None):
    """
    Parameterized test function for CRUD operations
    
    Args:
        action: CRUD_CREATE, CRUD_READ, CRUD_UPDATE, or CRUD_DELETE
        payload: JSON payload for POST/PUT operations
        resource_id: ID for GET/UPDATE/DELETE operations
    """
    action_names = {
        CRUD_CREATE: "CREATE",
        CRUD_READ: "READ",
        CRUD_UPDATE: "UPDATE",
        CRUD_DELETE: "DELETE"
    }
    
    url = build_url(action, resource_id)
    method = get_http_method(action)
    
    logger.info(f"=== TEST: {action_names.get(action, 'UNKNOWN')} ===")
    logger.info(f"Method: {method} | URL: {url}")
    
    try:
        if method == "POST":
            response = requests.post(url, json=payload)
        elif method == "GET":
            response = requests.get(url)
        elif method == "PUT":
            response = requests.put(url, json=payload)
        elif method == "DELETE":
            response = requests.delete(url)
        
        logger.info(f"Status Code: {response.status_code}")
        
        if response.status_code in [200, 201]:
            logger.info(f"Response: {json.dumps(response.json(), indent=2)}")
            return response.json()
        else:
            logger.error(f"Error Response: {response.text}")
            return None
            
    except Exception as e:
        logger.error(f"Test failed: {e}")
        return None

def test_proximity_search(latitude: float, longitude: float, distance: float, test_name: str = ""):
    """
    Test proximity search endpoint
    
    Args:
        latitude: User's latitude
        longitude: User's longitude
        distance: Search radius in km
        test_name: Description of the test
    """
    url = f"{BASE_URL}{ENDPOINT}nearby?latitude={latitude}&longitude={longitude}&distance={distance}"
    
    logger.info(f"=== TEST: PROXIMITY SEARCH {test_name} ===")
    logger.info(f"URL: {url}")
    logger.info(f"Search Center: ({latitude}, {longitude}), Radius: {distance} km")
    
    try:
        response = requests.get(url)
        logger.info(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Found {data['total_found']} locations")
            logger.info(f"Response: {json.dumps(data, indent=2)}")
            return data
        else:
            logger.error(f"Error Response: {response.text}")
            return None
            
    except Exception as e:
        logger.error(f"Proximity search test failed: {e}")
        return None

# ===== RUN TESTS =====
if __name__ == "__main__":
    logger.info("Starting CRUD Tests...\n")
    # test_crud(CRUD_UPDATE, PAYLOAD_UPDATED, resource_id=3)  # Update (future)
    # Test READ ALL
    # logger.info(">>> Testing READ ALL operation END <<<")
    # all_data = test_crud(CRUD_READ)
    
    # ===== PROXIMITY SEARCH TESTS =====
    logger.info(">>> Test 1: Proximity search near Manila (5 km radius) <<<")
    test_proximity_search(14.5994, 120.9842, 5.0, "- Manila Area")
    logger.info("")
    
    logger.info(">>> Test 2: Proximity search near New York (10 km radius) <<<")
    test_proximity_search(40.7128, -74.0060, 10.0, "- NYC Area")
    logger.info("")
    
    logger.info(">>> Test 3: Proximity search with small radius (1 km from Manila) <<<")
    test_proximity_search(14.5994, 120.9842, 1.0, "- Very Close")
    logger.info("")
    
    logger.info(">>> Test 4: Invalid distance - too small (0.01 km) <<<")
    test_proximity_search(14.5994, 120.9842, 0.01, "- Invalid: Too Small")
    logger.info("")
    
    logger.info(">>> Test 5: Invalid distance - too large (100,000 km) <<<")
    test_proximity_search(14.5994, 120.9842, 100000.0, "- Invalid: Too Large")
    logger.info("")
    
    logger.info(">>> Test 6: Invalid latitude (95 degrees) <<<")
    test_proximity_search(95.0, 120.9842, 5.0, "- Invalid: Bad Latitude")
    logger.info("")

    # test_crud(CRUD_READ)
    logger.info("")
    logger.info("All tests completed!")