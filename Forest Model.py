import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (replace 'imputed_data.xlsx' with your actual file path)
file_path = r'C:\Users\keros\.venv\Capstone-Project\imputed_data.xlsx'
df = pd.read_excel(file_path)

# Specify the columns for the scatter plot (replace 'Population 2023' and 'Annual' with your desired columns)
x_column = 'Facility Total'
y_column = 'Annual'

# Create a scatter plot
plt.scatter(df[x_column], df[y_column])
plt.title(f'Scatter Plot of {y_column} vs {x_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.grid(True)
plt.show()
