import pandas as pd
import csv
from datetime import datetime

def extract_ic_data(ic_attendance_csv)
    ic_attendance = {}
    with open(ic_attendance_csv, mode='r', encoding='utf-8-sig') as att_file:
        reader = csv.DictReader(att_file)
        next(reader)
        for row in reader:
            personID = row['personID']
            periodID = row['periodID']
            status = row['status']
            excuseIDmodifiedDate = row['excuseIDmodifiedDate']
            if personID not in


def extract_student_demographics(student_demographics_csv)
    with open(student_demographics_csv, mode='r', encoding='utf-8-sig') as stu_file:
        student_demographics = {}
        reader = csv.DictReader(stu_file)
        next(reader)
        for row in reader:
            personID = row['personID']
            student_number = row['student_number']
            first_name = row['first_name']
            last_name = row['last_name']
            middle_name = row['middle_name']
            if personID not in student_demographics:

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