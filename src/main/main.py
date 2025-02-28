from ..extract import edmentum_session_data_extract as edmentum_extract
from ..extract import infinite_campus_attendance_extract as ic_att_extract
from ..extract import infinite_campus_student_demographics_extract as students
from ..transform import edmentum_session_processing as edmentum_transform
from ..transform import infinite_campus_attendance_processing as ic_att_transform
from ..transform import legacy_attendance_transform as legacy


def main():
    start: bool = True
    SESSION_THRESHOLD = 5  # 5 minutes or greater is the time needed to be counted present
    while start:
        choice = input("Please choose: ")
        print("A - Process Edmentum Sessions")
        print("B - Process Infinite Campus Attendance")
        print("C - Process student demographics")
        print("D - Process legacy attendance")
        print("E - Combine attendance")
        print("F - Export to csv")
        print("G - Quit Application")
        match choice:
            case "A":
                # Get edmentum sessions
                online_session_data = edmentum_extract.extract_student_sessions(edmentum_session_data)
                edmentum_extract.print_attendance(online_session_data)
                # Transform edmentum sessions
                edmentum_transform.transform_student_sessions(online_session_data, SESSION_THRESHOLD)
            case "B":
                # Get infinite campus attendance
                attendance_data = ic_att_extract.extract_ic_data(ic_attendance)
                ic_att_extract.print_attendance(attendance_data)
                # Transform infinite campus attendance
                ic_att_transform.process_attendance(attendance_data)
            case "C":
                # Get student info
                student_data = students.extract_student_demographics(ic_student_demographics)
                students.print_student_demographics(student_data)
                # Transform student info
            case "D":
                # Transform legacy attendance
                legacy.transform_legacy_attendance(legacy_attendance)
            case "E":
                # Join student info with attendance data
            case "F":
                # Export to csv
            case "G":
                start = False
                break


# File paths
edmentum_session_data = \
    "../../data/raw/edmentum/LearnerDailyUsageReportByUserAndClass_GroupByLearner_CSV_hartjr@OAED_01292025082928.csv"
ic_attendance = \
    "../../data/raw/infinite_campus/icstudentattendance.csv"
ic_student_demographics = \
    "../../data/raw/infinite_campus/student_demographics"
legacy_attendance = None

if __name__ == "__main__":
    main()
