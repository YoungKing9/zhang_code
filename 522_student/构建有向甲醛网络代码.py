import folium
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests  # 处理请求
import json  # 将json文件解析为Python字典或列表
import matplotlib.cm as cm  # 绘制点
import matplotlib.colors as colors  # 绘制点
# from pandas.io.json import json_normalize  # 将json文件转换为pandas数据框
# from geopy.geocoders import Nominatim  # 对需要的不同区域的经度和纬度进行地理编码
# from sklearn.cluster import KMeans  # 用于创建k-means模型

from folium.plugins import MarkerCluster

dataa = pd.read_csv('/Users/86131/Desktop/工作日_普通_虹口.csv')
dataa1 = pd.read_csv('/Users/86131/Desktop/工作日_普通_宝山.csv')
dataa2 = pd.read_csv('/Users/86131/Desktop/工作日_普通_嘉定.csv')
dataa3 = pd.read_csv('/Users/86131/Desktop/工作日_普通_静安.csv')
dataa4 = pd.read_csv('/Users/86131/Desktop/工作日_普通_黄埔.csv')
dataa5 = pd.read_csv('/Users/86131/Desktop/工作日_普通_普陀.csv')
dataa6 = pd.read_csv('/Users/86131/Desktop/工作日_普通_徐汇.csv')
dataa7 = pd.read_csv('/Users/86131/Desktop/工作日_普通_杨浦.csv')
dataa8 = pd.read_csv('/Users/86131/Desktop/工作日_普通_闵行.csv')
dataa9 = pd.read_csv('/Users/86131/Desktop/工作日_普通_长宁.csv')
dataa10 = pd.read_csv('/Users/86131/Desktop/工作日_普通_浦东新区.csv')

latitude = dataa.end_locati
longitude = dataa.end_loca_1

latitude1 = dataa1.end_locati
longitude1 = dataa1.end_loca_1

latitude2 = dataa2.end_locati
longitude2 = dataa2.end_loca_1

latitude3 = dataa3.end_locati
longitude3 = dataa3.end_loca_1

latitude4 = dataa4.end_locati
longitude4 = dataa4.end_loca_1

latitude5 = dataa5.end_locati
longitude5 = dataa5.end_loca_1

latitude6 = dataa6.end_locati
longitude6 = dataa6.end_loca_1

latitude7 = dataa7.end_locati
longitude7 = dataa7.end_loca_1

latitude8 = dataa8.end_locati
longitude8 = dataa8.end_loca_1

latitude9 = dataa9.end_locati
longitude9 = dataa9.end_loca_1

latitude10 = dataa10.end_locati
longitude10 = dataa10.end_loca_1

print(latitude, longitude, latitude1, longitude1, latitude2, longitude2, latitude3, longitude3,
      latitude4, longitude4, latitude5, longitude5, latitude6, longitude6, latitude7, longitude7,
      latitude8, longitude8, latitude9, longitude9, latitude10, longitude10)

from sklearn.cluster import KMeans

kclusters = 5
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(dataa[['end_locati', 'end_loca_1']])
kmeans.labels_[0:10]

dataa.insert(0, 'Cluster Labels1', kmeans.labels_)
dataa.head()

kclusters1 = 3
kmeans1 = KMeans(n_clusters=kclusters1, random_state=0).fit(dataa1[['end_locati', 'end_loca_1']])
kmeans1.labels_[0:10]

dataa1.insert(0, 'Cluster Labels1', kmeans1.labels_)
dataa1.head()

kclusters2 = 3
kmeans2 = KMeans(n_clusters=kclusters2, random_state=0).fit(dataa2[['end_locati', 'end_loca_1']])
kmeans2.labels_[0:10]

dataa2.insert(0, 'Cluster Labels1', kmeans2.labels_)
dataa2.head()

kclusters3 = 4
kmeans3 = KMeans(n_clusters=kclusters3, random_state=0).fit(dataa3[['end_locati', 'end_loca_1']])
kmeans3.labels_[0:10]

dataa3.insert(0, 'Cluster Labels1', kmeans3.labels_)
dataa3.head()

# （以下省略不写，与上述相同）


cluster_map = folium.Map(location=[31.15, 121.32], zoom_start=12)

# set colors for the clusters
x = np.arange(kclusters)
ys = [i + x + (i * x) ** 2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]
centers = kmeans.cluster_centers_

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

x1 = np.arange(kclusters1)
ys1 = [i + x1 + (i * x1) ** 2 for i in range(kclusters1)]
colors_array1 = cm.rainbow(np.linspace(0, 1, len(ys1)))
rainbow1 = [colors.rgb2hex(i) for i in colors_array1]
centers1 = kmeans1.cluster_centers_

for lat1, lon1, village1, cluster1 in zip(dataa1.end_loca_1, dataa1.end_locati, dataa1['orderid'],
                                          dataa1['Cluster Labels1']):
    label1 = folium.Popup(str(village1) + ' Cluster ' + str(cluster1), parse_html=True)
    folium.CircleMarker(
        [lat1, lon1],
        radius=5,
        popup=label1,
        color=rainbow1[cluster1 - 1],
        fill=True,
        fill_color=rainbow1[cluster1 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x2 = np.arange(kclusters2)
ys2 = [i + x2 + (i * x2) ** 2 for i in range(kclusters)]
colors_array2 = cm.rainbow(np.linspace(0, 1, len(ys2)))
rainbow2 = [colors.rgb2hex(i) for i in colors_array2]
centers2 = kmeans2.cluster_centers_

for lat2, lon2, village2, cluster2 in zip(dataa2.end_loca_1, dataa2.end_locati, dataa2['orderid'],
                                          dataa2['Cluster Labels1']):
    label2 = folium.Popup(str(village2) + ' Cluster ' + str(cluster2), parse_html=True)
    folium.CircleMarker(
        [lat2, lon2],
        radius=5,
        popup=label2,
        color=rainbow2[cluster2 - 1],
        fill=True,
        fill_color=rainbow2[cluster2 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x3 = np.arange(kclusters)
ys3 = [i + x3 + (i * x3) ** 2 for i in range(kclusters)]
colors_array3 = cm.rainbow(np.linspace(0, 1, len(ys3)))
rainbow3 = [colors.rgb2hex(i) for i in colors_array3]
centers3 = kmeans3.cluster_centers_

for lat3, lon3, village3, cluster3 in zip(dataa3.end_loca_1, dataa3.end_locati, dataa3['orderid'],
                                          dataa3['Cluster Labels1']):
    label3 = folium.Popup(str(village3) + ' Cluster ' + str(cluster3), parse_html=True)
    folium.CircleMarker(
        [lat3, lon3],
        radius=5,
        popup=label3,
        color=rainbow3[cluster3 - 1],
        fill=True,
        fill_color=rainbow3[cluster3 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x4 = np.arange(kclusters)
ys4 = [i + x4 + (i * x4) ** 2 for i in range(kclusters)]
colors_array4 = cm.rainbow(np.linspace(0, 1, len(ys4)))
rainbow4 = [colors.rgb2hex(i) for i in colors_array4]
# centers4 = kmeans4.cluster_centers_

for lat4, lon4, village4, cluster4 in zip(dataa4.end_loca_1, dataa4.end_locati, dataa4['orderid'],
                                          dataa4['Cluster Labels1']):
    label4 = folium.Popup(str(village4) + ' Cluster ' + str(cluster4), parse_html=True)
    folium.CircleMarker(
        [lat4, lon4],
        radius=5,
        popup=label4,
        color=rainbow4[cluster4 - 1],
        fill=True,
        fill_color=rainbow4[cluster4 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x5 = np.arange(kclusters)
ys5 = [i + x5 + (i * x5) ** 2 for i in range(kclusters)]
colors_array5 = cm.rainbow(np.linspace(0, 1, len(ys5)))
rainbow5 = [colors.rgb2hex(i) for i in colors_array5]
# centers5 = kmeans5.cluster_centers_

for lat5, lon5, village5, cluster5 in zip(dataa5.end_loca_1, dataa5.end_locati, dataa5['orderid'],
                                          dataa5['Cluster Labels1']):
    label5 = folium.Popup(str(village5) + ' Cluster ' + str(cluster5), parse_html=True)
    folium.CircleMarker(
        [lat5, lon5],
        radius=5,
        popup=label5,
        color=rainbow5[cluster5 - 1],
        fill=True,
        fill_color=rainbow5[cluster5 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x6 = np.arange(kclusters)
ys6 = [i + x6 + (i * x6) ** 2 for i in range(kclusters)]
colors_array6 = cm.rainbow(np.linspace(0, 1, len(ys6)))
rainbow6 = [colors.rgb2hex(i) for i in colors_array6]
# centers6 = kmeans6.cluster_centers_

for lat6, lon6, village6, cluster6 in zip(dataa6.end_loca_1, dataa6.end_locati, dataa6['orderid'],
                                          dataa6['Cluster Labels1']):
    label6 = folium.Popup(str(village6) + ' Cluster ' + str(cluster6), parse_html=True)
    folium.CircleMarker(
        [lat6, lon6],
        radius=5,
        popup=label6,
        color=rainbow6[cluster6 - 1],
        fill=True,
        fill_color=rainbow6[cluster6 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x7 = np.arange(kclusters)
ys7 = [i + x7 + (i * x7) ** 2 for i in range(kclusters)]
colors_array7 = cm.rainbow(np.linspace(0, 1, len(ys7)))
rainbow7 = [colors.rgb2hex(i) for i in colors_array7]
# centers7 = kmeans7.cluster_centers_

for lat7, lon7, village7, cluster7 in zip(dataa7.end_loca_1, dataa7.end_locati, dataa7['orderid'],
                                          dataa7['Cluster Labels1']):
    label7 = folium.Popup(str(village7) + ' Cluster ' + str(cluster7), parse_html=True)
    folium.CircleMarker(
        [lat7, lon7],
        radius=5,
        popup=label7,
        color=rainbow7[cluster7 - 1],
        fill=True,
        fill_color=rainbow7[cluster7 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x8 = np.arange(kclusters)
ys8 = [i + x8 + (i * x8) ** 2 for i in range(kclusters)]
colors_array8 = cm.rainbow(np.linspace(0, 1, len(ys8)))
rainbow8 = [colors.rgb2hex(i) for i in colors_array8]
# centers8 = kmeans8.cluster_centers_

for lat8, lon8, village8, cluster8 in zip(dataa8.end_loca_1, dataa8.end_locati, dataa8['orderid'],
                                          dataa8['Cluster Labels1']):
    label8 = folium.Popup(str(village8) + ' Cluster ' + str(cluster8), parse_html=True)
    folium.CircleMarker(
        [lat8, lon8],
        radius=5,
        popup=label8,
        color=rainbow8[cluster8 - 1],
        fill=True,
        fill_color=rainbow8[cluster8 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x9 = np.arange(kclusters)
ys9 = [i + x9 + (i * x9) ** 2 for i in range(kclusters)]
colors_array9 = cm.rainbow(np.linspace(0, 1, len(ys9)))
rainbow9 = [colors.rgb2hex(i) for i in colors_array9]
# centers9 = kmeans9.cluster_centers_

for lat9, lon9, village9, cluster9 in zip(dataa9.end_loca_1, dataa9.end_locati, dataa9['orderid'],
                                          dataa9['Cluster Labels1']):
    label9 = folium.Popup(str(village9) + ' Cluster ' + str(cluster9), parse_html=True)
    folium.CircleMarker(
        [lat9, lon9],
        radius=5,
        popup=label9,
        color=rainbow9[cluster9 - 1],
        fill=True,
        fill_color=rainbow9[cluster9 - 1],
        fill_opacity=0.7).add_to(cluster_map)

x10 = np.arange(kclusters)
ys10 = [i + x10 + (i * x10) ** 2 for i in range(kclusters)]
colors_array10 = cm.rainbow(np.linspace(0, 1, len(ys10)))
rainbow10 = [colors.rgb2hex(i) for i in colors_array10]
# centers10 = kmeans10.cluster_centers_

for lat10, lon10, village10, cluster10 in zip(dataa10.end_loca_1, dataa10.end_locati, dataa10['orderid'],
                                              dataa10['Cluster Labels1']):
    label10 = folium.Popup(str(village10) + ' Cluster ' + str(cluster10), parse_html=True)
    folium.CircleMarker(
        [lat10, lon10],
        radius=5,
        popup=label10,
        color=rainbow10[cluster10 - 1],
        fill=True,
        fill_color=rainbow10[cluster10 - 1],
        fill_opacity=0.7).add_to(cluster_map)

cluster_map