# Data-acquisition-test

**This is the explanation of the functions used in the test**
- `download_and_unzip_data(url, output, path)`:  Download and unzip the customers-100.zip file
- `read_data(file_path)`: Read the extracted csv file with pandas library
- `compute_rows(dataframe)`: Return the number of columns in a dataframe
- `compute_columns(dataframe)`: Return the number of columns in a dataframe
- `show_rows_and_columns(dataframe)`: Write the results of numbers of rows and columns to rows_and_columns.txt file
- `snake_case_column_names(dataframe)`:Replace the column names to snake-case

**How to run the python script:**

- Install the dependencies using the following command in the terminal:
```python
pip install -r requirements.txt
```

- Run the Python Code

```python
python test.py
```