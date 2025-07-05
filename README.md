# 🏫 Attendance ETL Pipeline

This project automates the extraction, transformation, and loading of student attendance data from multiple sources to produce a clean, consolidated CSV for upload into a Student Information System (SIS).

> ⚠️ **Note:** This project is a work in progress. Core functionality and integration logic are still being developed.

---

## 📑 Table of Contents
- [Project Overview](#project-overview)
- [Goals](#goals)
- [Data Sources](#data-sources)
- [ETL Workflow](#etl-workflow)
- [Technologies Used](#technologies-used)
- [Output](#output)
- [Folder Structure](#folder-structure)
- [Planned Improvements](#planned-improvements)


---

## 📌 Project Overview

Schools using both **in-person attendance systems** and **online learning platforms** (like Edmentum) often struggle to maintain accurate, unified attendance records—especially for hybrid or remote learners. This pipeline was developed to reconcile discrepancies by identifying students who were not marked present in-person but were active online for a sufficient amount of time (e.g., 10 minutes).

The solution was designed to support **weekly reporting** for school leadership by automating the consolidation of attendance data into a single, structured file. This improved visibility into overall attendance patterns and reduced the reliance on manual processes across systems.

---

## 🎯 Goals

- Automatically extract and clean data from multiple platforms
- Detect and flag students who should be marked present based on online activity
- Generate a clean, SIS-ready `.csv` file for batch attendance updates
- Support **weekly attendance reporting** to school leadership by enabling repeatable and automated data refreshes  

---

## 📂 Data Sources

- **Infinite Campus** — In-person attendance logs and student demographics  
- **Edmentum** — Online session activity for virtual learners

---

## 🔄 ETL Workflow

### 1. **Extract**
- `edmentum_session_data_extract.py`
- `infinite_campus_attendance_extract.py`
- `infinite_campus_student_demographics_extract.py`

### 2. **Transform**
- Remove duplicates
- Convert timestamps with `datetime`
- Calculate online session durations
- **Students were flagged as present if their total online session time exceeded a custom threshold (e.g., 10 minutes), allowing reconciliation with in-person attendance records.**
- Join with demographics and attendance records

### 3. **Load**
- Final dataset exported as a `.csv` for upload to Infinite Campus or another SIS

---

## 🧰 Technologies Used

- **Python 3**
- **Pandas** — data manipulation
- **datetime** — time comparisons and duration calculations
- **Logging** (optional) — to monitor extract/load success

---

## 📤 Output

A final `.csv` file is generated, ready for upload into the SIS. Each record includes:

- Student ID  
- Date  
- Attendance status (present/absent)  
- Source of presence (in-person or virtual)  

---

## 📁 Folder Structure

```
attendance-etl/
├── main/
│   └── main.py
├── extract/
│   ├── edmentum_session_data_extract.py
│   ├── infinite_campus_attendance_extract.py
│   └── infinite_campus_student_demographics_extract.py
├── transform/
│   ├── edmentum_session_processing.py
│   ├── infinite_campus_attendance_processing.py
│   └── legacy_attendance_transform.py
├── load/
│   └── (optional: load logic or output handler)
└── output/
    └── attendance_upload.csv
```

---

## 🚀 Planned Improvements

While this project is still in progress, the following improvements were planned to enhance automation, scalability, and maintainability:

- **Cloud Deployment**  
  Convert the ETL script into an AWS Lambda function to run on a scheduled basis (e.g., weekly via CloudWatch Events or EventBridge).

- **Database Integration**  
  Store attendance records in a cloud-based database such as **Amazon DynamoDB**, partitioned by `student_id` and sorted by `date` for fast querying and dashboard integration.

- **One-Time Legacy Data Import**  
  Process the manually tracked attendance from the Google Sheet once and merge it into the final system for historical completeness.

- **Dashboard or API Layer** *(future idea)*  
  Expose attendance data via a simple internal dashboard or API for school staff to review attendance history without relying on spreadsheets.



---

## 👤 Author

**Jalen Terrell-Hart**  
[GitHub Profile](https://github.com/Jalenhart4)
