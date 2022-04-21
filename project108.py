import pandas as pd
import csv
import plotly.figure_factory as pf

data = pd.read_csv("project108.csv")

avgrating = data["Avg Rating"].tolist()

graph = pf.create_distplot([avgrating], ["Average rating graph"], show_hist=False)


graph.show()











