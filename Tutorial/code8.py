from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

app = Dash(external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div([
    html.H1("Calculator"),
    html.Br(),
    html.Div([
            html.Label("Enter first number "),
            dcc.Input(id='x', value=0, type='number', style={'margin':'5px','marginLeft':'30px'}),
            html.Br(),
            html.Label("Select Operator "),
            dcc.Dropdown( ['+','-','*','/'],'+',id='op',style={'width': '100px','display': 'inline-block', 'marginLeft':'67px'}),
            html.Br(),
            html.Label("Enter second number "),
            dcc.Input(id='y', value=0, type='number', style={'margin':'5px','marginLeft':'7px'})
        ]),
    html.Br(),
    html.Label("Answer "),
    html.Div(id='ans'),
])

@app.callback(
    Output('ans','children'),
    Input('x','value'),
    Input('op','value'),
    Input('y','value')
)

def update_output_div(x,op,y):
    opr = operatorlookup.get(op)
    return opr(float(x),float(y))

if __name__ == '__main__':
    app.run()