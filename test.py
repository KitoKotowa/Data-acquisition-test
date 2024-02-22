import pandas as pd
import gdown

from shutil import unpack_archive

"""
This is the explanation of the functions used in the test
- download_and_unzip_data(url, output, path):  Download and unzip the customers-100.zip file
- read_data(file_path): Read the extracted csv file with pandas library
- compute_rows(dataframe): Return the number of columns in a dataframe
- compute_columns(dataframe): Return the number of columns in a dataframe
- show_rows_and_columns(dataframe): Write the results of numbers of rows and columns to rows_and_columns.txt file
- snake_case_column_names(dataframe):Replace the column names to snake-case

How to run the python script:
- Install the dependencies using the following command in the terminal:
    pip install -r requirements.txt
- Run the Python Code: 
    python test.py
"""

def download_and_unzip_data(url, output, path):
    gdown.download(url, output, quiet=False)
    unpack_archive(output, path)
    print(f"File downloaded and extracted at {output}")

def read_data(file_path):
    return pd.read_csv(file_path)

def compute_rows(dataframe):
    return len(dataframe.axes[0])

def compute_columns(dataframe):
    return len(dataframe.axes[1])

def show_rows_and_columns(dataframe):
    rows = compute_rows(dataframe)
    cols = compute_columns(dataframe)
    with open("rows_and_columns.txt", "w") as file:
        file.write(f"The dataset has {rows} rows and {cols} columns.")
    
def snake_case_column_names(dataframe):
    dataframe.columns = dataframe.columns.str.lower().str.replace(' ','_')
    return dataframe

def init():
    url = "https://drive.google.com/uc?id=1yyL20BNKv3PxJRJVjJ_2Q-HidvIUis45&export=download"
    output = "data/customers-100.zip"
    path = "data"
    result_path = "data/result.csv"
    
    download_and_unzip_data(url, output, path)
    #url = strip_url(url)
    customer_data = read_data("data/customers-100.csv")
    show_rows_and_columns(customer_data)
    customer_data = snake_case_column_names(customer_data)
    customer_info = pd.DataFrame(customer_data, columns=['index', 'customer_id', 'first_name', 'last_name', 'phone_1'])
    customer_info.to_csv(result_path)
    print(customer_info)

    print(f"File exported at {result_path}")

def main():
    init()

if __name__=="__main__": 
    main() 

