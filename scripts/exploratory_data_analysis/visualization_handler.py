
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt




def plot_categorical_bar_chart(df, variable):
    unique_values = df[variable].unique()
    value_counts = df[variable].value_counts()

    # Create a DataFrame with unique values and their counts
    data = pd.DataFrame({variable: unique_values, 'Count': value_counts})

    # Create bar chart
    fig = px.bar(data, x=variable, y='Count', title=f'Bar Chart of {variable}')

    fig.update_layout(width=800, height=600)

   
    fig.show()


def plot_histogram(dataset, variable, bar_width=0.8):
    # Check if the variable is numeric
    if dataset[variable].dtype != 'object':
        # Create a histogram plot for the variable
        fig = px.histogram(dataset, x=variable, title=f'Histogram of {variable}')
        fig.update_traces(marker_line_width=bar_width)
        fig.show()
    else:
        print("The variable is not numeric.")



def plot_stats(data):
    variables = list(data.columns)
    measurements = ['Range', 'Variance', 'Standard Deviation']
    colors = ['red', 'green', 'blue']
    
    if len(variables) > len(colors):
        colors = colors * (len(variables) // len(colors) + 1)

    fig = go.Figure()

    for i, variable in enumerate(variables):
        values = data.loc[:, variable].values
        fig.add_trace(go.Bar(
            x=measurements,
            y=values,
            name=variable,
            marker_color=colors[i]
        ))

    fig.update_layout(
        title='Measurements for Variables',
        xaxis_title='Measurement',
        yaxis_title='Value'
    )
    fig.update_layout(width=800, height=600)
    fig.show()




def visualize_and_correlate(df):
    # Scatter plot
    fig = px.scatter(df, x='PremiumChange', y='ClaimsChange', color='PostalCode')
    fig.update_layout(
        xaxis_title='Monthly Change in TotalPremium',
        yaxis_title='Monthly Change in TotalClaims',
        title='Scatter Plot - Monthly Changes in TotalPremium vs TotalClaims'
    )
    fig.show()

    # Correlation matrix
    correlation_matrix = df.groupby('PostalCode')[['PremiumChange', 'ClaimsChange']].corr().unstack()['ClaimsChange']['PremiumChange']
    return correlation_matrix





def detect_outliers(dataset, numerical_variable):

    fig = go.Figure()
    fig.add_trace(go.Box(y=dataset[numerical_variable], name=numerical_variable))
    fig.show()
    
    q1 = dataset[numerical_variable].quantile(0.25)
    q3 = dataset[numerical_variable].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = dataset[(dataset[numerical_variable] < lower_bound) | (dataset[numerical_variable] > upper_bound)][numerical_variable].tolist()
    
    #return outliers

