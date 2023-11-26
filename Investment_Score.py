import pandas as pd

# Load the combined data from the output file
output_file_path = r'C:\Users\keros\.venv\Capstone-Project\outputdata.xlsx'
combined_data = pd.read_excel(output_file_path)

# Your scoring calculations here
combined_data['Investment_Score'] = (
    combined_data['Gross Patient Revenue'] / 1000 +
    combined_data['Total Deficiencies'] * 0.5 +
    combined_data['Fines'] * 0.8
)

# Sort by the Investment_Score in descending order
sorted_data = combined_data.sort_values(by='Investment_Score', ascending=False)

# Select the top and bottom 10 rows
top_10 = sorted_data.head(10)
bottom_10 = sorted_data.tail(10)

# Print the top and bottom 10 states
print("Top 10 States:")
print(top_10)

print("\nBottom 10 States:")
print(bottom_10)

# Concatenate the top and bottom 10 subsets
result_data = pd.concat([top_10, bottom_10])

# Set the path for the output Excel file
output_result_path = r'C:\Users\keros\.venv\Capstone-Project\investment_results.xlsx'

# Write the results to the output Excel file without including the index
result_data.to_excel(output_result_path, index=False)

print(f"\nTop and bottom 10 investment results saved to {output_result_path}")
