
import plotly.express as px
import pandas as pd

def plot_categorical_bar_chart(df, variable):
    unique_values = df[variable].unique()
    value_counts = df[variable].value_counts()

    # Create a DataFrame with unique values and their counts
    data = pd.DataFrame({variable: unique_values, 'Count': value_counts})

    # Create the bar chart using Plotly Express
    fig = px.bar(data, x=variable, y='Count', title=f'Bar Chart of {variable}')

    # Show the chart
    fig.show()


