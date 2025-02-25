from extract import edmentum_session_data_extract as edmentum
from extract import infinite_campus_attendance_extract as ic_att
from extract import infinite_campus_student_demographics_extract as students

def main():
    try:
        online_session_data = edmentum.extract_student_sessions(raw_edmentum_session_data, session_threshold)
        edmentum.print_attendance(online_session_data)

        attendance_data = ic_att.extract_ic_data(ic_attendance_csv)
        ic_att.print_attendance(attendance_data)

        student_data = students.extract_student_demographics(ic_student_demographics_csv)
        students.print_student_demographics(student_data)
    except Exception as e:
        print(f"An error occurred: \n {e}")

# Config
session_threshold = 5  # 5 minutes or greater is the time needed to be counted present

# File paths
raw_edmentum_session_data = "../../data/raw/edmentum/LearnerDailyUsageReportByUserAndClass_GroupByLearner_CSV_hartjr@OAED_01292025082928.csv"
ic_attendance_csv = "../../data/raw/infinite_campus/icstudentattendance.csv"
ic_student_demographics_csv = "../../data/raw/infinite_campus/student_demographics"
if __name__ == "__main__":
    main()