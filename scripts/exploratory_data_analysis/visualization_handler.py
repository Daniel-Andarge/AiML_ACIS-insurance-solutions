import pandas as pd
import matplotlib.pyplot as plt

def plot_numerical_histograms(df, column):

        plt.figure(figsize=(8, 6))
        df[column].plot.hist(bins=10)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

def plot_categorical_barcharts(df, column):
   
        plt.figure(figsize=(8, 6))
        df[column].value_counts().plot.bar()
        plt.title(f'Bar Chart of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

