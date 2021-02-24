import pandas as pd
import plotly_express as px
df = pd.read_csv("data2.csv")
fig = px.scatter(df, x="date", y="cases",color="country")
fig.show()
#it works but its backwards and looks like trash