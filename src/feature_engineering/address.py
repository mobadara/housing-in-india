from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="house_price_prediction_app")


def get_full_address(address: str) -> str:
    """
    Given a partial address, return the full standardized address using geocoding.

    Args:
        address (str): The partial address to be standardized.
    Returns:
        str: The full standardized address.
    """
    
    location = geolocator.geocode(address)
    if location:
        return location.address
    else:
        return "Address not found"
    
def get_address_from_coordinates(lat: float, lon: float) -> str:
    """
    Given latitude and longitude, return the full address using reverse geocoding.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
    Returns:
        str: The full address corresponding to the given coordinates.
    """
    
    location = geolocator.reverse((lat, lon))
    if location:
        return location.address
    else:
        return 'Address not found'  
