import csv
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")

def get_district(lat, lon):
    location = geolocator.reverse((lat, lon), exactly_one=True)
    if location:
        address = location.raw['address']
        district = address.get('suburb') or address.get('town')
        return district
    return None


filename = 'house_prices.csv'


output_filename = 'updated_dataset.csv'

with open(filename, 'r') as file, open(output_filename, 'w', newline='') as output_file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['district']
    
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    # Iterate over each record in the CSV file
    for row in csv_reader:
        try:
            lat = float(row['lat'])  # Latitude value for the record
            lon = float(row['lng'])  # Longitude value for the record
            
            district = get_district(lat, lon)
            
            if district:
                row['district'] = district
            else:
                row['district'] = "Unknown"  # Set a default value if district is not found
            
            csv_writer.writerow(row)
        except Exception as e :
            print(str(e))
print("Dataset updated and saved to", output_filename)
