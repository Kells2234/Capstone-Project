import pandas as pd

# Assuming you have a DataFrame with a 'Score' column
data = {'Name': ['Student1', 'Student2', 'Student3'],
        'Score': [85, 92, 78]}
df = pd.DataFrame(data)

# Define the assign_grade function
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Apply the assign_grade function to the 'Score' column
df['Grade'] = df['Score'].apply(assign_grade)

# Display the DataFrame with the assigned grades
print(df)
