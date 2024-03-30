import pandas as pd
import numpy as np
import dash
from dash import dcc, html, callback 
from dash.dependencies import Input, Output
import plotly.express as px


inf = pd.read_csv('adult.data.csv')

# Generate random salaries within the specified ranges
random_salaries_below_50k = np.random.randint(20000, 50001, size=len(inf))
random_salaries_above_50k = np.random.randint(50001, 80001, size=len(inf))

# Modify the "salary" column based on the condition
inf['salary'] = np.where(inf['salary'] == '<=50K', random_salaries_below_50k, random_salaries_above_50k)

# Initialize the Dash app
app = dash.Dash(__name__)

#App layout
app.layout = html.Div([
    html.Div(children='Demographic data visualization', style={'textAlign':'center'}),
    html.Hr(),
    dcc.Dropdown(id='dropdown', options=[{'label': i, 'value': i} for i in ['native-country', 'sex']], value='native-country', multi=False),
    dcc.RadioItems(options=['salary', 'age', 'hours-per-week'], value='salary', id='buttons'),
    dcc.Graph(figure={}, id='graphs')
])

#implement interactivity
@callback(
    Output(component_id='graphs', component_property='figure'),
    Input(component_id='buttons', component_property='value'),
    Input(component_id='dropdown', component_property='value')
)

def my_graph(pick, selected_dropdown):
    if selected_dropdown == 'native-country':
        fig = px.histogram(inf, x='native-country', y=pick, histfunc='avg')
    else:
        fig = px.histogram(inf, x='sex', y=pick, histfunc='avg')
    
    return fig   
 
#Run the app
if __name__ == '__main__':
    app.run(debug=True)


print(inf.head())
print(inf.columns)
print(inf.shape)