import folium
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# define the city map
city_map = folium.Map(location=[31.15, 121.32], zoom_start=8)
# display city map
city_map
m = folium.Map(location=[31.15, 121.32],zoom_start=8)
m.add_child(folium.LatLngPopup())
m

from folium.plugins import MarkerCluster

data = pd.read_csv('/Users/86131/Desktop/上海摩拜8月工作日.csv')
data.head()

limit = 3000
data = data.iloc[0:limit, :]

# Instantiate a feature group for the incidents in the dataframe
#为数据框中的事件实例化功能组
incidents = folium.map.FeatureGroup()

# Loop through the 200 crimes and add each to the incidents feature group
#循环浏览200个犯罪，并将每个犯罪添加到事件功能组
for lat, lng, in zip(data.end_location_y, data.end_location_x):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=4, # define how big you want the circle markers to be

            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=0.4
        )
    )

# Add incidents to map
san_map = folium.Map(location=[lat, lng], zoom_start=12)
san_map.add_child(incidents)