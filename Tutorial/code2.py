# Drop down
from dash import Dash, html, dcc

app = Dash()
app.title = "Hello World!"
app.layout = html.Div(
    children = [
        html.H1(app.title),
        html.H3("Department"),
        dcc.Dropdown(
            options = [
                {'label' : "Mechanical", 'value' : 1},
                {'label' : "Electrical", 'value' : 2},
                {'label' : "Computer Science", 'value' : 3},
                {'label' : "Civil", 'value' : 4},
            ],
            value = "2",
            multi = True
        ),
    ]
)

if __name__ == "__main__":
    app.run()