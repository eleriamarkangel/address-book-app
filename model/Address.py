from pydantic import BaseModel, field_validator

class Address(BaseModel):
    latitude: float
    longitude: float
    address: dict

    @field_validator("latitude", "longitude")
    def check_floating_point(cls, v):
        if not isinstance(v, float):
            raise ValueError("Latitude and longitude must be floating point numbers")
        return round(v, 8)