# Define the grading criteria
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

# Read data from the output file
file_path = r'C:\Users\keros\.venv\Capstone-Project\output_data.xlsx'
with open('output_data.xlsx', 'r') as file:
    lines = file.readlines()

# Process each line and assign grades
grades = []
for line in lines:
    try:
        score = float(line.strip())  # Assuming the data is numerical
        grade = assign_grade(score)
        grades.append(grade)
    except ValueError:
        print(f"Skipping invalid data: {line}")

# Display or save the grades as needed
print("Grades:")
for i, grade in enumerate(grades, start=1):
    print(f"Student {i}: {grade}")




