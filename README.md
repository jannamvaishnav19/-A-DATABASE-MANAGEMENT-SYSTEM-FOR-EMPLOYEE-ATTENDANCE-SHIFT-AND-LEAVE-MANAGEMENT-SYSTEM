<<<<<<< HEAD
# StaffTrack — Employee Attendance, Shift & Leave Management System

A GitHub-ready demo application based on the StaffTrack screen references. It includes a Flask web interface, SQLite persistence, six UI screenshots, three project-review presentations, and a quick-start guide.

## Features
- Dashboard metrics and recent attendance
- Employee records: add and list employees
- Shift configuration: create and list shifts
- Attendance recording and history
- Leave requests with approve/reject actions
- Attendance and leave summary reports
- Responsive styling inspired by the supplied screenshots

## Requirements
- Python 3.10 or later
- pip

## Run locally
From the project root:

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. A local SQLite database is created automatically in `instance/stafftrack.sqlite`.

## Push to GitHub
Create an empty repository on GitHub, then run these commands from this folder:

```bash
git init
git add .
git commit -m "Add StaffTrack application and review materials"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the example remote URL with your actual GitHub repository URL.

## Repository layout

```text
StaffTrack-GitHub/
├── app.py
├── requirements.txt
├── README.md
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── routes.py
│   ├── static/style.css
│   └── templates/
├── database/
├── screenshots/
└── presentations/
```

## Important scope note
This is a small runnable demo aligned to the supplied screen references. It is not yet the complete 12-table database implementation described in the review slides; authentication, roster assignment, overtime workflows, leave-balance accounting, and the full set of seven SQL report views would need to be added for full parity with those deliverables. Do not use demo data for real employee records.
=======
# -A-DATABASE-MANAGEMENT-SYSTEM-FOR-EMPLOYEE-ATTENDANCE-SHIFT-AND-LEAVE-MANAGEMENT-SYSTEM
A DBMS project to manage employee attendance, shifts, overtime, and leave balances. Features include roster scheduling, clock-in/out tracking, leave approvals, and attendance reports. Built using Python or Java with MySQL, PostgreSQL, or SQLite, ensuring data accuracy, integrity, and efficient management.
>>>>>>> b7e73d7bfc4daade85cb0d77560bc86d6ac3da5d
