import pandas as pd
import os

# Set the path to the directory containing your Excel files
input_directory = r'C:\Users\keros\.venv\Capstone-Project'

# List all files in the directory
all_files = os.listdir(input_directory)

# Specify desired columns for each file
desired_columns_nursing_home = ['State', 'Region', 'Private Room Annual Cost', 'Shared Room Annual Cost']

desired_columns_occ_rate = ['Occupancy Rate Avg']

desired_columns_population_stats = ['Population 2023']

desired_columns_facility_staffing_combined = ['Staff Average', 'Staff Increase/Decrease']

desired_columns_state_violations = ['Total Deficiencies', 'Fine', 'Sum of Fines']

desired_columns_mapping = {
    'Nursing home Cost_state.xlsx': desired_columns_nursing_home,
    'Occ rate 2015_2023.xlsx': desired_columns_occ_rate,
    'Population_stats.xlsx': desired_columns_population_stats,
    'Facility Staffing Combined.xlsx': desired_columns_facility_staffing_combined,
    'State by State Violations2023.xlsx': desired_columns_state_violations
}

# Filter Excel files
excel_files = [f for f in all_files if f.endswith('.xlsx')]

# Iterate through each Excel file
for excel_file in excel_files:
    excel_path = os.path.join(input_directory, excel_file)

    # Determine which desired_columns list to use based on the file
    desired_columns = desired_columns_mapping.get(excel_file, [])
    if not desired_columns:
        print(f"Desired columns not specified for {excel_file}. Skipping...")
        continue

    # Read the Excel file with the specified desired_columns
    df = pd.read_excel(excel_path, usecols=desired_columns)

# Filter CSV files
csv_files = [f for f in all_files if f.endswith('.csv')]

desired_columns_facility_by_state = ['Facility Total']

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Print the column names in each Excel sheet
for excel_file in excel_files:
    excel_path = os.path.join(input_directory, excel_file)
    df = pd.read_excel(excel_path)
    print(f"Columns in {excel_file}: {df.columns}")

# Columns you want to include in the final DataFrame
desired_columns = ['State', 'Region', 'Private Room Annual Cost', 'Shared Room Annual Cost',
                   'Facility Total', 'Population 2023', 'Staff Average ', 'Staff Increase/Decrease',
                   'Total Deficiencies', 'Fines', 'Sum of Fines']

# Loop through each Excel file and append its data to the combined DataFrame
for excel_file in excel_files:
    # Skip temporary Excel files
    if excel_file.startswith('~$'):
        continue

    excel_path = os.path.join(input_directory, excel_file)
    try:
        # Print columns before reading
        print(f"Columns in {excel_file}: {pd.read_excel(excel_path, nrows=0).columns}")

        df = pd.read_excel(excel_path, usecols=desired_columns)  # Assumes data is in the first sheet, adjust as needed

        # Check if 'State' column exists
        if 'State' in df.columns:
            # Add State_ID to the DataFrame based on State names
            state_id_mapping = {state: idx + 1 for idx, state in enumerate(df['State'].unique())}
            df['State_ID'] = df['State'].map(state_id_mapping)

            combined_data = pd.concat([combined_data, df], ignore_index=True)
        else:
            print(f"'State' column not found in {excel_file}. Skipping...")
    except pd.errors.ParserError as e:
        print(f"Error reading {excel_file}: {e}")

# Loop through each CSV file and append its data to the combined DataFrame
for csv_file in csv_files:
    csv_path = os.path.join(input_directory, csv_file)
    try:
        df = pd.read_csv(csv_path, usecols=desired_columns)

        # Check if 'State' column exists
        if 'State' in df.columns:
            # Add State_ID to the DataFrame based on State names
            state_id_mapping = {state: idx + 1 for idx, state in enumerate(df['State'].unique())}
            df['State_ID'] = df['State'].map(state_id_mapping)

            combined_data = pd.concat([combined_data, df], ignore_index=True)
        else:
            print(f"'State' column not found in {csv_file}. Skipping...")
    except pd.errors.ParserError as e:
        print(f"Error reading {csv_file}: {e}")

# Set the path for the output Excel file
output_file_path = r'C:\Users\keros\.venv\Capstone-Project\output_data.xlsx'

# Write the combined data to the output Excel file
combined_data.to_excel(output_file_path, index=False)

print(f"Data from {len(excel_files)} Excel files and {len(csv_files)} CSV files combined and saved to {output_file_path}")
