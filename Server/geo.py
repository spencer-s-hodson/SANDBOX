# from geopy.geocoders import Nominatim
# from geopy.distance import great_circle

# class AddressComparator:
#     def __init__(self):
#         self.geolocator = Nominatim(user_agent="address_comparator")

#     def geocode_address(self, address):
#         """Geocode a given address to latitude and longitude."""
#         location = self.geolocator.geocode(address)
#         if location:
#             return (location.latitude, location.longitude)
#         else:
#             raise ValueError(f"Address '{address}' could not be geocoded")

#     def calculate_distance(self, address1, address2):
#         """Calculate the great-circle distance between two addresses."""
#         location1 = self.geocode_address(address1)
#         location2 = self.geocode_address(address2)
#         return great_circle(location1, location2).kilometers

# # Example usage
# comparator = AddressComparator()
# distance = comparator.calculate_distance("1690 N Canyon Road, Provo, UT", "5279 Roxanne Ct., Livermore, CA")
# print(distance)