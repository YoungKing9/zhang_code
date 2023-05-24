import requests
import xlwt
import pandas as pd
import numpy as np
from tqdm import tqdm
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

posi = pd.read_csv('/Users/86131/Desktop/a/总.csv')
posi = posi.dropna()
posi.head()

lat = np.array(posi["end_loca_1"][0:len(posi)])
lon = np.array(posi["end_locati"][0:len(posi)])
gdp = np.array(posi["Cluster Labels2"][0:len(posi)],dtype=float)
data1 = [[lat[i],lon[i]] for i in range(len(posi))]

data1

map_osm  = folium.Map(location=[31.150000, 121.320000], zoom_start=12)
HeatMap(data1).add_to(map_osm)
map_osm