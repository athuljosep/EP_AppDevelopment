# Theme
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.PULSE])
app.title = "Hello World!"
app.layout = html.Div(
    children = [
        html.H1(app.title),
        html.H3("Department"),
        dcc.Dropdown(
            id = 'dept_dropdown',
            options = [
                {'label' : "Mechanical", 'value' : 1},
                {'label' : "Electrical", 'value' : 2},
                {'label' : "Computer Science", 'value' : 3},
                {'label' : "Civil", 'value' : 4},
            ],
            value = "2",
            multi = True
        ),
        html.Button(
            style={'width' : '100%'},
            id = 'select_all_button',
            children = ["Select all"]
        )
    ]
)

@app.callback(
    Output('dept_dropdown','value'),
    Input('select_all_button','n_clicks'),
    prevent_initial_call = True
)

def select_all(select_all_button):
    return [1,2,3,4]

if __name__ == "__main__":
    app.run()