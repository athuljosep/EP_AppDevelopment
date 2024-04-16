# Basic
from dash import Dash, html

app = Dash()
app.title = "Hello World!"
app.layout = html.Div(
    html.H1(app.title)
)

if __name__ == "__main__":
    app.run()