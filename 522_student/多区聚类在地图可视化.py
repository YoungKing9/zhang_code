import folium
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests  # 处理请求
import json  # 将json文件解析为Python字典或列表
import matplotlib.cm as cm  # 绘制点
import matplotlib.colors as colors  # 绘制点
from pandas.io.json import json_normalize  # 将json文件转换为pandas数据框
from geopy.geocoders import Nominatim  # 对需要的不同区域的经度和纬度进行地理编码
from sklearn.cluster import KMeans  # 用于创建k-means模型

# define the city map
city_map = folium.Map(location=[31.15, 121.32], zoom_start=8)
# display city map
city_map
m = folium.Map(location=[31.15, 121.32], zoom_start=12)
m.add_child(folium.LatLngPopup())
m

from folium.plugins import MarkerCluster

dataa = pd.read_csv('/Users/86131/Desktop/工作日_普通_虹口.csv')
dataa.head()

latitude1 = dataa.end_locati
longitude1 = dataa.end_loca_1
print(latitude1, longitude1)

dataaa = pd.read_csv('/Users/86131/Desktop/工作日_普通_宝山.csv')
dataaa.head()

latitude = dataaa.end_locati
longitude = dataaa.end_loca_1
print(latitude, longitude)

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10)
kmeans

from sklearn.cluster import KMeans

kclusters = 10
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(dataa[['end_locati', 'end_loca_1']])
kmeans.labels_[0:10]

kclusters = 10
kmeanss = KMeans(n_clusters=kclusters, random_state=0).fit(dataaa[['end_locati', 'end_loca_1']])
kmeanss.labels_[0:10]

dataa.insert(0, 'Cluster Labels1', kmeans.labels_)
dataa.head()

dataaa.insert(0, 'Cluster Labels1', kmeanss.labels_)
dataaa.head()

cluster_map = folium.Map(location=[31.15, 121.32], zoom_start=12)

# set colors for the clusters
x = np.arange(kclusters)
ys = [i + x + (i * x) ** 2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]
centers = kmeans.cluster_centers_

# put markers
cluster_markers = []
for lat, lon, village, cluster in zip(dataa.end_loca_1, dataa.end_locati, dataa['orderid'], dataa['Cluster Labels1']):
    label = folium.Popup(str(village) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster - 1],
        fill=True,
        fill_color=rainbow[cluster - 1],
        fill_opacity=0.7).add_to(cluster_map)

xs = np.arange(kclusters)
yss = [i + xs + (i * xs) ** 2 for i in range(kclusters)]
colors_arrays = cm.rainbow(np.linspace(0, 1, len(yss)))
rainbows = [colors.rgb2hex(i) for i in colors_arrays]
centerss = kmeanss.cluster_centers_

for lat1, lon1, village1, cluster1 in zip(dataaa.end_loca_1, dataaa.end_locati, dataaa['orderid'],
                                          dataaa['Cluster Labels1']):
    label1 = folium.Popup(str(village1) + ' Cluster ' + str(cluster1), parse_html=True)
    folium.CircleMarker(
        [lat1, lon1],
        radius=5,
        popup=label1,
        color=rainbows[cluster1 - 1],
        fill=True,
        fill_color=rainbows[cluster1 - 1],
        fill_opacity=0.7).add_to(cluster_map)
cluster_map