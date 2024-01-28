from geopy.geocoders import Nominatim
from geopy.distance import great_circle

class AddressComparator:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="address_comparator")
        self.large_distance = 1e7  # A very large distance in kilometers

    def geocode_address(self, address):
        """Geocode a given address to latitude and longitude."""
        location = self.geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            raise ValueError(f"Address '{address}' could not be geocoded")

    def calculate_distance(self, address1, address2):
        """Calculate the great-circle distance between two addresses or return a large distance if address is invalid."""
        try:
            location1 = self.geocode_address(address1)
            location2 = self.geocode_address(address2)
            return great_circle(location1, location2).kilometers
        except ValueError:
            return self.large_distance
