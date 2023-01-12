from google.colab import files
d = files.upload()


import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

height = df["Height"].tolist()
weight = df["Weight"].tolist()

fig = px.scatter(x=height, y=weight)
fig.show()


import numpy as np
height_array = np.array(height)
weight_array = np.array(weight)

#Slope and intercept using pre-built function of Numpy
m, c = np.polyfit(height_array, weight_array, 1)

y = []
for x in height_array:
  y_value = m*x + c
  y.append(y_value)

#plotting the graph
fig = px.scatter(x=height_array, y=weight_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(height_array), x1= max(height_array)
    )
])
fig.show()