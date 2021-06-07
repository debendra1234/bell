import plotly.figure_factory as ff
import pandas as pd
import csv
df=pd.read_csv("data12345.csv")
fig=ff.create_distplot([df["Mobile Brand"].tolist()],["Mobile"],show_hist=False)
fig.write_html('first_figure.html', auto_open=True)