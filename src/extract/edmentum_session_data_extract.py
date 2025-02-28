"""
This is a Script to Extract student Edmentum sessions for attendance reporting.
The threshold for if a student is counted as present for that day is if the session last more than the threshold.
"""
import csv
from datetime import datetime
import pandas as pd


def parse_datetime(datetime_str):
    """Parses a datetime string into a datetime object."""
    return datetime.strptime(datetime_str, "%m/%d/%Y %I:%M:%S %p")


def extract_student_sessions(csv_file):
    """ Extracts student session data from CSV.
            Fields Extracted:
            LearnerFirstName (String),
            LearnerLastname (String),
            LoginDateTime (DateTime),
            LogOutDateTime (DateTime) """
    df = pd.read_csv(csv_file, parse_dates=["LoginDateTime", "LogOutDateTime"])
    return df


def print_attendance(student_attendance):
    """Prints the attendance record in a readable format."""
    for student, dates in student_attendance.items():
        print(f"{student}: {sorted(dates)}")

