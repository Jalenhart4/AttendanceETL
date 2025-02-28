import pandas as pd


def extract_ic_data(ic_attendance_csv):
    """
    Extracts raw attendance records from infinite campus.
    Fields extracted:
        personID (int)
        periodID (int) - 17 = AM 18 = PM
        status (char)
        modifiedDate (Date)
    """
    # Load the Infinite Campus attendance data into a pandas DataFrame
    ic_df = pd.read_csv(ic_attendance_csv, encoding='utf-8-sig')
    return ic_df


def print_attendance(ic_attendance):
    """Prints the attendance record in a readable format."""
    for student, dates in ic_attendance.items():
        print(f"{student}: {sorted(dates)}")
