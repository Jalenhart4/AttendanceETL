import pandas as pd

def extract_student_demographics(student_demographics_csv):
    """
    Raw Student Demographic data
    Fields extracted:
        personID (int),
        studentNumber (int),
        firstName (string),
        lastName (string),
        middleName (string)
    """
    # Load the student demographics data into a pandas DataFrame
    stu_df = pd.read_csv(student_demographics_csv, encoding='utf-8-sig')

    # Create a dictionary with personID as the key
    student_demographics = stu_df.set_index('personID').to_dict(orient='index')

    return student_demographics

def print_student_demographics(student_demographics):
    """Prints the attendance record in a readable format."""
    for student, dates in student_demographics.items():
        print(f"{student}: {sorted(dates)}")

