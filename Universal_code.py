import pandas as pd
import os

# Set the path to the directory containing your Excel files
input_directory = r'C:\Users\keros\.venv\Capstone-Project'

# Initialize a dictionary to store DataFrames for each file
dfs = {}

# List all files in the directory
all_files = os.listdir(input_directory)

# Loop through each file and read its data into the dictionary
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

        # Specify desired columns based on actual columns
        desired_columns = [col for col in actual_columns if col in [
            'State', 'Region', 'Private Room Annual Cost', 'Shared Room Annual Cost',
            'Employee Average', 'Staff Increase/Decrease', 'Population 2023',
            'Total Deficiencies', 'Fines', 'Sum of Fines', 'Facility Total'
        ]]

        dfs[excel_file] = pd.read_excel(excel_path, usecols=desired_columns)

    except Exception as e:
        print(f"Error reading {excel_file}: {e}")

# Concatenate all DataFrames in the dictionary
combined_data = pd.concat([df for df in dfs.values()], axis=1)

# Set the path for the output Excel file
output_file_path = r'C:\Users\keros\.venv\Capstone-Project\outputdata.xlsx'

# Write the combined data to the output Excel file
combined_data.to_excel(output_file_path, index=False)

print(f"Data from {len(all_files)} Excel files combined and saved to {output_file_path}")
