# Dropdown and Graph
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(external_stylesheets=[dbc.themes.PULSE])

app.layout = html.Div([
    html.H1(children='Plotly Graph', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Dropdown(df.columns[3:], 'pop', id='dropdown-selection1'),
    dcc.Graph(id='graph-content'),
])

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('dropdown-selection1', 'value')
)

def update_graph(value1,value2):
    dff = df[df.country==value1]
    return px.line(dff, x='year', y=value2)

if __name__ == '__main__':
    app.run()
