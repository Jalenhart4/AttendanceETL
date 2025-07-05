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

---

## 📌 Project Overview

Schools using both **in-person** attendance systems and **online platforms** (like Edmentum) often struggle to accurately track student attendance. This pipeline reconciles discrepancies by identifying students who were not marked present in-person but were active online long enough to meet a custom threshold.

---

## 🎯 Goals

- Automatically extract and clean data from multiple platforms
- Detect and flag students who should be marked present based on online activity
- Generate a clean, SIS-ready `.csv` file for batch attendance updates

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

## 📤 Output

A final `.csv` file is generated, ready for upload into the SIS. Each record includes:

- Student ID  
- Date  
- Attendance status (present/absent)  
- Source of presence (in-person or virtual)  

---

## 👤 Author

**Jalen Terrell-Hart**  
[GitHub Profile](https://github.com/Jalenhart4)
