import folium
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests # 处理请求
import json # 将json文件解析为Python字典或列表
import matplotlib.cm as cm # 绘制点
import matplotlib.colors as colors # 绘制点
from pandas.io.json import json_normalize # 将json文件转换为pandas数据框
from geopy.geocoders import Nominatim # 对需要的不同区域的经度和纬度进行地理编码
from sklearn.cluster import KMeans # 用于创建k-means模型

# define the city map
city_map = folium.Map(location=[31.15, 121.32], zoom_start=8)
# display city map
city_map
m = folium.Map(location=[31.15, 121.32],zoom_start=12)
m.add_child(folium.LatLngPopup())
m

from folium.plugins import MarkerCluster
dataa = pd.read_csv('/Users/86131/Desktop/上海摩拜8月工作日.csv')
dataa.head()

latitude = dataa.end_location_y
longitude = dataa.end_location_y
print(latitude, longitude)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=10)
kmeans

incidents = folium.map.FeatureGroup()

for lat, lng, in zip(dataa.end_location_y, dataa.end_location_x):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=3,
            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=4
        )
    )
san_map = folium.Map(location=[lat, lng], zoom_start=12)
san_map.add_child(incidents)

from sklearn.cluster import KMeans
kclusters = 10
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(dataa[[ 'end_location_x', 'end_location_y']])
kmeans.labels_[0:10]

dataa.insert(0, 'Cluster Labels', kmeans.labels_)

dataa.head()

cluster_map = folium.Map(location=[31.15, 121.32], zoom_start=12)

# set colors for the clusters
x = np.arange(kclusters)
ys = [i + x + (i*x)**2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]
centers = kmeans.cluster_centers_

# put markers
cluster_markers = []
for lat, lon, village, cluster in zip(dataa.end_location_y, dataa.end_location_x, dataa['orderid'], dataa['Cluster Labels']):
    label = folium.Popup(str(village) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(cluster_map)
cluster_map