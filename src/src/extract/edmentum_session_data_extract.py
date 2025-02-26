"""
This is a Script to Extract student Edmentum sessions for attendance reporting.
The threshold for if a student is counted as present for that day is if the session last more than the threshold.
"""
import csv
from datetime import datetime


def parse_datetime(datetime_str):
    """Parses a datetime string into a datetime object."""
    return datetime.strptime(datetime_str, "%m/%d/%Y %I:%M:%S %p")


def extract_student_sessions(csv_file,session_threshold):
    """ Processes student session data and stores attendance records in dictionary.
        Fields Extracted:
            LearnerFirstName (String),
            LearnerLastname (String),
            LoginDateTime (DateTime),
            LogOutDateTime (DateTime)
    """
    student_attendance = {}
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        next(reader)
        # print("CSV Headers:", reader.fieldnames)
        for row in reader:
            last_name = row["LearnerLastName"]
            first_name = row["LearnerFirstName"].lstrip("\ufeff")
            login_time = parse_datetime(row["LoginDateTime"].strip())
            logout_time = parse_datetime(row["LogOutDateTime"].strip())

            session_duration = (logout_time - login_time).total_seconds() / 60  # Convert to minutes
            session_date = login_time.date()

            if session_duration > session_threshold:
                student_key = f"{last_name} {first_name}"
                if student_key not in student_attendance:
                    student_attendance[student_key] = set()
                student_attendance[student_key].add(session_date)

    return student_attendance

def print_attendance(student_attendance):
    """Prints the attendance record in a readable format."""
    for student, dates in student_attendance.items():
        print(f"{student}: {sorted(dates)}")

