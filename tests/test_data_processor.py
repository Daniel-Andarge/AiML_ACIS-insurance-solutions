import pandas as pd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts/data_preparation_utils'))

# Import all functions from the directory
from text_to_dataframe import text_to_dataframe
from load_dataset import load_dataset
from format_data import format_data
from find_missing_values import find_missing_values
from handle_missing_values import handle_missing_values
from save_dataset import save_dataset

def test_text_to_dataframe():
    path = "data/text_data.txt"
    df = text_to_dataframe(path)

    assert isinstance(df, pd.DataFrame), "text_to_dataframe should return a DataFrame"

    expected_columns = ["Column1", "Column2", "Column3"]
    assert all(col in df.columns for col in expected_columns), "text_to_dataframe should return a DataFrame with the expected columns"


def test_load_dataset():
    path = "data/dataset.csv"
    df = load_dataset(path)

    # Check if the returned value is a DataFrame
    assert isinstance(df, pd.DataFrame), "load_dataset should return a DataFrame"

    # Check if the DataFrame has the expected columns
    expected_columns = ["Column1", "Column2", "Column3"]
    assert all(col in df.columns for col in expected_columns), "load_dataset should return a DataFrame with the expected columns"

   

def test_format_data():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({"TransactionMonth": ["2022-01-01", "2022-02-01", "2022-03-01"],
                       "Column1": [1, 2, 3],
                       "Column2": [4, 5, 6]})
  
    formatted_df = format_data(df)

    # Check if the "TransactionMonth" column is converted to datetime
    assert isinstance(formatted_df["TransactionMonth"].dtype, pd.core.dtypes.dtypes.DatetimeTZDtype), "format_data should convert 'TransactionMonth' column to datetime"

    # Check if the object columns are converted to string
    object_columns = formatted_df.select_dtypes(include="object").columns
    assert all(formatted_df[col].dtype == str for col in object_columns), "format_data should convert object columns to string"

    
def test_find_missing_values():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({"Column1": [1, 2, None],
                       "Column2": [None, 5, 6],
                       "Column3": [7, 8, 9]})

    missing_values = find_missing_values(df)

    # Check if the returned value is a Series
    assert isinstance(missing_values, pd.Series), "find_missing_values should return a Series"

    # Check if the missing values are correctly calculated
    expected_missing_values = pd.Series({"Column1": 1, "Column2": 1, "Column3": 0})
    assert missing_values.equals(expected_missing_values), "find_missing_values should correctly calculate missing values"

    

def test_handle_missing_values():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({"Column1": [1, 2, None],
                       "Column2": [None, 5, 6],
                       "Column3": [7, 8, 9]})

    filled_df = handle_missing_values(df)

    # Check if the returned value is a string
    assert isinstance(filled_df, str), "handle_missing_values should return a string"

    
def test_save_dataset():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({"Column1": [1, 2, 3],
                       "Column2": [4, 5, 6],
                       "Column3": [7, 8, 9]})

    output_folder = "output"
    filename = "output.csv"

    output_path = save_dataset(df, output_folder, filename)

    # Check if the output folder and file are created
    assert os.path.exists(output_folder), "save_dataset should create the output folder"
    assert os.path.isfile(output_path), "save_dataset should save the dataset file"

 
test_text_to_dataframe()
test_load_dataset()
test_format_data()
test_find_missing_values()
test_handle_missing_values()
test_save_dataset()