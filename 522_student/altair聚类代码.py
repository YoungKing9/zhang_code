import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/86131/Desktop/上海摩拜8月工作日.csv')
data.head()

limit = 4980
data = data.iloc[0:limit, :]
alt.Chart(data).mark_circle(size=100).encode(
    x='end_location_x',
    y='end_location_y',
    color='start_time'
).interactive()

from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=10)

kmeans

data.columns

kmeans.fit(data[[ 'start_location_x', 'start_location_y', 'end_location_x', 'end_location_y']])
data['label']=kmeans.labels_
data.groupby('label').size()

alt.Chart(data).mark_circle(size=50).encode(
    x='end_location_x',
    y='end_location_y',
    color=alt.Color('label:N')
).configure_axis(
    grid=False
).interactive(
).properties(
    width=4500,
    height=1000
)

sse=[]
for k in range(1,22):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(data[[ 'start_location_x', 'start_location_y', 'end_location_x', 'end_location_y']])
    sse.append(kmeans.inertia_)
sse

plt.plot(range(1,22),sse)