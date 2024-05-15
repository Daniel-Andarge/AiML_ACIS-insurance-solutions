


import pandas as pd

def calculate_variability(df, columns):
    result = {}
    for col in columns:
        data = df[col]
        result[col] = {
            'Range': data.max() - data.min(),
            'Variance': data.var(),
            'Standard Deviation': data.std()
        }

        df_variability = pd.DataFrame(result)
    return df_variability

