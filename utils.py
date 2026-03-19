from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    
    Returns distance in kilometers
    """
    # Earth's radius in km
    R = 6371.0
    
    # Convert degrees to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    
    # Differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    
    return distance

def validate_distance(distance: float) -> tuple[bool, str]:
    """
    Validate distance bounds for proximity search
    
    Returns: (is_valid, error_message)
    """
    MIN_DISTANCE = 0.1  # 100 meters
    MAX_DISTANCE = 50000  # 50,000 km (roughly half earth's circumference)
    
    if distance < MIN_DISTANCE:
        return False, f"Distance must be at least {MIN_DISTANCE} km"
    if distance > MAX_DISTANCE:
        return False, f"Distance cannot exceed {MAX_DISTANCE} km"
    
    return True, ""
