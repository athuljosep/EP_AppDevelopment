# This function helps to test individual functionalities
import plotly.express as px
import pandas as pd

# Sample data
data = {'values': [10, 20, 30, 40, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]}
df = pd.DataFrame(data)


data1 = {'values1': [100, 200, 300, 400, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]}
df1 = pd.DataFrame(data1)

# Create histogram
fig = px.histogram(df, x='values')
fig1 = px.histogram(df1, x='values1')
line_trace = fig1.data[0]
fig.add_trace(line_trace)

# Update x-axis label
fig.update_layout(xaxis_title='Value Distribution')



# Show plot
fig.show()