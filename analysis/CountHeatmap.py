import folium
import pandas as pd


df = pd.read_csv('preprocess/cleaned_dataset.csv')


district_counts = df['district'].value_counts().reset_index()
district_counts.columns = ['district', 'count']


tehran_geojson = 'preprocess/tehran_districts.geojson'


tehran_coordinates = [35.6892, 51.3890]
map_tehran = folium.Map(location=tehran_coordinates, zoom_start=11)


folium.Choropleth(
    geo_data=tehran_geojson,
    name='choropleth',
    data=district_counts,
    columns=['district', 'count'],
    key_on='feature.properties.district',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Advertise Count'
).add_to(map_tehran)


folium.LayerControl().add_to(map_tehran)


map_tehran.save("analysis/result/CountHeatmap.html")
