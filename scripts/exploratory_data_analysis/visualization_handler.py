
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def plot_categorical_bar_chart(df, variable):
    unique_values = df[variable].unique()
    value_counts = df[variable].value_counts()

    # Create a DataFrame with unique values and their counts
    data = pd.DataFrame({variable: unique_values, 'Count': value_counts})

    # Create the bar chart using Plotly Express
    fig = px.bar(data, x=variable, y='Count', title=f'Bar Chart of {variable}')

    # Show the chart
    fig.show()




def plot_histogram(data, column, bins=10):
    # Calculate the range for the histogram bins
    min_value = np.min(data[column])
    max_value = np.max(data[column])
    bin_range = (max_value - min_value) / bins

    # Create the histogram plot using Plotly
    fig = go.Figure(data=[go.Histogram(x=data[column], xbins=dict(start=min_value, end=max_value, size=bin_range))])

    # Customize the histogram plot
    fig.update_layout(
        title=f'Histogram of {column}',
        xaxis_title=column,
        yaxis_title='Count',
        bargap=0.1  # Adjust the gap between bars
    )

    # Show the plot
    fig.show()


