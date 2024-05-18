

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



def calculate_changes(dataset):
 
    selected_columns = ['PostalCode', 'TotalPremium', 'TotalClaims']

    # drop missing values if any
    dataset = dataset[selected_columns].dropna()

    # calculate monthly changes 
    dataset['PremiumChange'] = dataset.groupby('PostalCode')['TotalPremium'].diff()
    dataset['ClaimsChange'] = dataset.groupby('PostalCode')['TotalClaims'].diff()

    return dataset




