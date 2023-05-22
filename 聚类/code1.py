import numpy as np
import os
import folium
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

data=pd.read_csv('/Users/86131/Desktop/POIshujv3.csv')
data.head()
alt.data_transformers.enable('json')

limit = 150000
data = data.iloc[0:limit, :]
alt.Chart(data).mark_circle(size=50).encode(
    x='display_x',
    y='display_y',
    color='kind'
).interactive(
).properties(
    width=13500,
    height=3000
)
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=10)

kmeans
data.columns

kmeans.fit(data[[ 'display_x', 'display_y']])
data['label']=kmeans.labels_
data.groupby('label').size()

alt.Chart(data).mark_circle(size=50).encode(
    x='display_x',
    y='display_y',
    color=alt.Color('label:N')
).configure_axis(
    grid=False
).interactive(
)

sse=[]
for k in range(1,20):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(data[[ 'display_x', 'display_y']])
    sse.append(kmeans.inertia_)
sse

plt.plot(range(1,20),sse)