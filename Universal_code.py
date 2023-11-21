import pandas as pd
import os

# Set the path to the directory containing your Excel files
input_directory = r'C:\Users\keros\.venv\Capstone-Project'

# List all Excel files in the directory
excel_files = [f for f in os.listdir(input_directory) if f.endswith('Nursing home Cost_state.xlsx')]
excel_files = [f for f in os.listdir(input_directory) if f.endswith('Population_stats')]
excel_files = [f for f in os.listdir(input_directory) if f.endswith('Facility Staffing Combined.xlsx')]
excel_files = [f for f in os.listdir(input_directory) if f.endswith('State by State Violations2023.xlsx')]
csv_files = [f for f in os.listdir(input_directory) if f.endswith('Facility_by_state.csv')]


# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Columns you want to include in the final DataFrame
desired_columns = ['State', 'Population', 'GDP']

# Loop through each Excel file and append its data to the combined DataFrame
for excel_file in excel_files:
    excel_path = os.path.join(input_directory, excel_file)
    try:

        df = pd.read_excel(excel_path)  # Assumes data is in the first sheet, adjust as needed

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

    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Loop through each CSV file and append its data to the combined DataFrame
for csv_file in csv_files:
    csv_path = os.path.join(input_directory, csv_file)
    try:
        df = pd.read_csv(csv_path)

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
