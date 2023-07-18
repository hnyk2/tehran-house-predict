import folium
from folium.plugins import HeatMap
import pandas as pd

df = pd.read_csv('preprocess/cleaned_dataset.csv')

df['lat'] = df['lat'].str.replace('٫', '.').astype(float)
df['lng'] = df['lng'].str.replace('٫', '.').astype(float)




tehran_coordinates = [35.6892, 51.3890]
map_tehran = folium.Map(location=tehran_coordinates, zoom_start=12)


heat_data = [[row['lat'], row['lng'], row['price']] for index, row in df.iterrows()]


HeatMap(heat_data).add_to(map_tehran)


map_tehran.save("analysis/result/PriceHeatmap.html")
