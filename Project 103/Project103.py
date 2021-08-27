import pandas as pd
import plotly.express as px
df = pd.read_csv(r"C:/Users/Admin/Downloads/Project 103/Data.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "country", title = "Number of Covid-19 Cases in Different Countries")
fig.show()