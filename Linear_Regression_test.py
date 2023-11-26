import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Assuming your combined data is already loaded into a DataFrame
file_path = r"C:\Users\keros\.venv\Capstone-Project\outputdata.xlsx"

# Read the Excel file
combined_data = pd.read_excel(file_path)

# Assuming 'Gross Patient Revenue' is the target variable
target_variable = 'Gross Patient Revenue'

# Assuming other columns are potential features
potential_features = ['Monthly', 'Annual', 'Employee Average', 'Staff Increase/Decrease', 'Population 2023', 'Certified Beds by State']

# Selecting target variable and features from your combined data
features_and_target = combined_data[potential_features + [target_variable]]

# Drop any rows with missing values, if needed
features_and_target = features_and_target.dropna()

# Split the data into features (X) and target variable (y)
X = features_and_target.drop(target_variable, axis=1)
y = features_and_target[target_variable]

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize the predictions
plt.scatter(y_test, y_pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
