import pandas as pd
import numpy as np
import dash
from dash import dcc, html 
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px


inf = pd.read_csv('adult.data.csv')

# Generate random salaries within the specified ranges
random_salaries_below_50k = np.random.randint(20000, 50001, size=len(inf))
random_salaries_above_50k = np.random.randint(50001, 80001, size=len(inf))

# Modify the "salary" column based on the condition
inf['salary'] = np.where(inf['salary'] == '<=50K', random_salaries_below_50k, random_salaries_above_50k)

# Initialize the Dash app
app = Dash(__name__)



print(inf.head())
print(inf.columns)
print(inf.shape)