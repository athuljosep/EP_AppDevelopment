import pandas as pd

# Sample data for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}

# Create a DataFrame
df = pd.DataFrame(data)

columns=[{"name": i, "id": i} for i in df.columns]
data=df.to_dict('records')