import requests
import json
from logger import logger

# ===== GLOBAL VARIABLES =====
BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/geo-loc/"

# Test data payloads
PAYLOAD_MALACANAN = {
    "latitude": 14.5994,
    "longitude": 120.9842,
    "address": {
        "street": "J.P. Laurel Street",
        "city": "Manila",
        "country": "Philippines",
        "landmark": "Malacanan Palace"
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

# ===== RUN TESTS =====
if __name__ == "__main__":
    logger.info("Starting CRUD Tests...\n")
    # test_crud(CRUD_CREATE, PAYLOAD_MALACANAN)  # Create

    # Test READ ALL
    logger.info(">>> Testing READ ALL operation <<<")
    all_data = test_crud(CRUD_READ)
    logger.info("")
    
    logger.info(">>> Testing READ ONE operation <<<")
    test_crud(CRUD_READ, resource_id=1)
    
    # Test READ by invalid ID
    logger.info(">>> Testing READ by invalid ID (ID: 9999) <<<")
    invalid_read = test_crud(CRUD_READ, resource_id=9999)
    logger.info("")
    
    logger.info("✓ All tests completed!")

    # Just call test_crud() with the action
    # test_crud(CRUD_CREATE, PAYLOAD_MALACANAN)  # Create
    # test_crud(CRUD_READ)                       # Read all
    # test_crud(CRUD_READ, resource_id=1)        # Read one (future)
    # test_crud(CRUD_UPDATE, PAYLOAD_NEW, resource_id=1)  # Update (future)
    # test_crud(CRUD_DELETE, resource_id=1)      # Delete (future)