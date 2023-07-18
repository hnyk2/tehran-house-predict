from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="my_app")

# List of Tehran districts
districts = [
    "District 1",
    "District 2",
    "District 3",
    "District 4",
    "District 5",
    "District 6",
    "District 7",
    "District 8",
    "District 9",
    "District 10",
    "District 11",
    "District 12",
    "District 13",
    "District 14",
    "District 15",
    "District 16",
    "District 17",
    "District 18",
    "District 19",
    "District 20",
    "District 21",
    "District 22",
]


district_coordinates = []


for district in districts:
    location = geolocator.geocode(district + ", Tehran")
    if location:
        district_coordinates.append([location.latitude, location.longitude])
    else:
        print("Coordinates not found for", district)


for i, district in enumerate(districts):
    print(district, "coordinates:", district_coordinates[i])
