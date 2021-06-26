import pandas as pd
import plotly.express as px

df = pd.read_csv("Students Grade.csv")
fig = px.bar(df, x="student_roll.no", y="total marks")

fig.show()
