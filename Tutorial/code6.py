#  Graph Basic
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go

df = px.data.iris()  # iris is a pandas DataFrame
fig_1 = px.scatter(df, x="sepal_width", y="sepal_length")

fig_2 = go.Figure(data=[go.Scatter(x=[1, 2, 3, 4], y=[4, 1, 2, 8])])

app = Dash(external_stylesheets=[dbc.themes.PULSE])
app.title = "Basic Graphs"
app.layout = html.Div(
    children = [
        dcc.Graph(figure=fig_1),
        dcc.Graph(figure=fig_2),
        dcc.Graph(
            figure={
                'data': [
                    {'x': [2021, 2022, 2023], 'y': [34, 41, 42], 'type': 'bar', 'name': 'CS'},
                    {'x': [2021, 2022, 2023], 'y': [62, 74, 85], 'type': 'bar', 'name': 'EE'},
                ],
                'layout': {
                    'title': 'Journals Published',
                    'xaxis': {'title': 'Year'},
                    'yaxis': {'title': 'Number of Publications'},
                }
            }

        )
    ]
)

if __name__ == "__main__":
    app.run()