

# Data loading:

# Data Saving:

# Data cleaning:

# Data transformation: 

# Data quality checks: 

import pandas as pd
import os
import sys

def text_to_dataframe(path):
    try:
        # Convert text file into a DataFrame
        df = pd.read_csv(path, sep='|', low_memory=False)

        return df
    except FileNotFoundError as e:
        print(f"Error: {e}. The dataset file was not found.")
    except Exception as e:
        print(f"Error: {e}. An error occurred while loading the dataset.")
    return None

def load_dataset(path):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(path, low_memory=False)
        return df
    except FileNotFoundError as e:
        print(f"Error: {e}. The dataset file was not found.")
    except Exception as e:
        print(f"Error: {e}. An error occurred while loading the dataset.")
    return None


def format_data(df):
    # Convert object columns to string 
    object_columns = df.select_dtypes(include='object').columns
    df[object_columns] = df[object_columns].astype(str)

    # Convert TransactionMonth to datetime 
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    
    return df

def find_missing_values(df):
    missing_values = df.isnull().sum()
    #print(missing_values)
    return missing_values
    


def handle_missing_values(df):
   
   df_filled = "Missing"
   
#

   return df_filled



def handdle_outliers(df):



    return df_cleaned



def save_dataset(df, output_folder, filename):

    # Create  output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

 
    # Save cleaned dataset
    output_path = os.path.join(output_folder, filename)
    df.to_csv(output_path, index=False)

    print(f"Dataset saved to {output_path}")
    return output_path



