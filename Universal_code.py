import pandas as pd
import os

# Set the path to the directory containing your Excel files
input_directory = r'C:\Users\keros\.venv\Capstone-Project'

# Initialize a list to store DataFrames
dfs = []

# Specify the order of desired columns
desired_columns_order = [
    'State', 'Monthly', 'Annual', 'Employee Average', 'Staff Increase/Decrease',
    'Population 2023', 'Total Deficiencies', 'Fines', 'Sum of Fines', 'Facility Total', 'Certified Beds by State', 'Gross Point Revenue'
]

# List all files in the directory
all_files = os.listdir(input_directory)

# Loop through each file and read its data into the list
for excel_file in all_files:
    # Skip hidden files, directories, temporary Excel files, and non-Excel files
    if excel_file.startswith('.') or os.path.isdir(os.path.join(input_directory, excel_file)) \
            or excel_file.startswith('~$') or not excel_file.endswith('.xlsx'):
        continue

    excel_path = os.path.join(input_directory, excel_file)

    try:
        # Print columns before reading
        actual_columns = pd.read_excel(excel_path, nrows=0).columns
        print(f"Actual Columns in {excel_file}: {actual_columns}")

        # Specify desired columns based on actual columns and desired order
        desired_columns = [col for col in desired_columns_order if col in actual_columns]

        # Read the Excel file and select desired columns in the specified order
        df = pd.read_excel(excel_path, usecols=desired_columns)

        # Reorder columns to have 'State' as the first column
        df = df[['State'] + [col for col in desired_columns if col != 'State']]

        dfs.append(df)

    except Exception as e:
        print(f"Error reading {excel_file}: {e}")

# Concatenate all DataFrames in the list along the columns axis
if dfs:
    combined_data = pd.concat(dfs, axis=1)

    # Drop duplicate columns (if any)
    combined_data = combined_data.loc[:, ~combined_data.columns.duplicated()]

    # Set the path for the output Excel file
    output_file_path = r'C:\Users\keros\.venv\Capstone-Project\outputdata.xlsx'

    # Write the combined data to the output Excel file without including the index
    combined_data.to_excel(output_file_path, index=False)

    print(f"Data from {len(all_files)} Excel files combined and saved to {output_file_path}")
else:
    print("No valid data found in Excel files.")
