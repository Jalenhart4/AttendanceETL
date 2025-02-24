import pandas as pd
import csv
from datetime import datetime

def extract_ic_data(ic_attendance_csv):
    # Load the Infinite Campus attendance data into a pandas DataFrame
    ic_df = pd.read_csv(ic_attendance_csv, encoding='utf-8-sig')

    # Process the data into a dictionary grouped by personID
    ic_attendance = ic_df.groupby('personID').apply(lambda x: x[['periodID', 'status', 'excuseIDmodifiedDate']].to_dict(orient='records')).to_dict()

    return ic_attendance

def extract_student_demographics(student_demographics_csv):
    # Load the student demographics data into a pandas DataFrame
    stu_df = pd.read_csv(student_demographics_csv, encoding='utf-8-sig')

    # Create a dictionary with personID as the key
    student_demographics = stu_df.set_index('personID').to_dict(orient='index')

    return student_demographics

# File paths
"""
Raw attendance data from infinite campus. 
Fields extracted:
    personID (int)_
    periodID (int) - 17 = AM 18 = PM
    status (char) 
    excuseIDmodifiedDate (Date, )
"""
ic_attendance_csv = "../../data/raw/infinite_campus/icstudentattendance.csv"

"""
Student Demographics
Fields extracted:
    personID (int),
    studentNumber (int),
    firstName (string),
    lastName (string),
    middleName (string)
"""
student_demographics_csv = "../../data/raw/infinite_campus/student_demographics"

# Extract data
attendance_data = extract_ic_data(ic_attendance_csv)
student_data = extract_student_demographics(student_demographics_csv)