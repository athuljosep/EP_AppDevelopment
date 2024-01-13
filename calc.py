from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Calculator"),
    html.Div([
        dcc.Input(id='x', value=0, type='number'),
        dcc.Input(id='y', value=0, type='number')
    ],style={'width': '10%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown( ['+','-','*','/'],'+',id='op',)
    ],style={'width': '5%', 'display': 'inline-block'}),
    html.Br(),
    html.Div(id='ans'),
])

@callback(
    Output('ans','children'),
    Input('x','value'),
    Input('op','value'),
    Input('y','value')
)

def update_output_div(x,op,y):
    opr = operatorlookup.get(op)
    return opr(float(x),float(y))

if __name__ == '__main__':
    app.run(debug=True)