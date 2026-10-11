
# GITHUB UPLOAD GUIDE
## Employee Attendance, Shift and Leave Management System

### 1. Project Overview
This repository contains the source code, database scripts, documentation, review presentations, and final submission files for the Employee Attendance, Shift and Leave Management System.

### 2. Repository Structure

```text
Employee-Attendance-DBMS/
├── docs/
│   ├── screenshots/
│   ├── DATABASE_DESIGN.md
│   ├── ER_DIAGRAM.mmd
│   └── GITHUB_UPLOAD.md
├── presentations/
│   ├── Phase_1_Problem_Scope_ERD.pptx
│   ├── Phase_2_3NF_SQL_Queries.pptx
│   └── Phase_3_Application_Demo.pptx
├── sql/
│   ├── mysql_schema.sql
│   ├── report_queries.sql
│   └── schema_sqlite.sql
├── static/
│   ├── css/
│   └── js/
├── submission/
│   ├── Final_Report.pdf
│   └── Video_Presentation_Link.docx
├── templates/
├── tests/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### 3. Steps to Upload the Project

1. Create a new repository on GitHub.
2. Give it the name `Employee-Attendance-DBMS`.
3. Choose Public visibility if public access is required for submission.
4. Open the project folder in Visual Studio Code.
5. Open the terminal and initialize Git if it is not already initialized.
6. Stage and commit the project files.
7. Connect the local folder to the new GitHub repository.
8. Push the files to GitHub.
9. Open the repository in a browser and verify that the files are visible.

### 4. Git Commands

Run these commands from the project root folder. Replace the repository URL with your actual GitHub repository URL.

```bash
git init
git add .
git commit -m "Initial DBMS project upload"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

If the repository already has a remote named `origin`, check it using `git remote -v` instead of adding it again.

### 5. Required Deliverables

- Phase 1 presentation: Problem statement, objectives, scope, requirements, and ER diagram.
- Phase 2 presentation: Normalization up to 3NF, database schema, SQL queries, and constraints.
- Phase 3 presentation: Application implementation, prototype demonstration, and results.
- Working application and database scripts.
- Final project report in the prescribed format.
- Screenshots of the running application.
- Five-minute video presentation link.

### 6. Google Drive Video Submission

1. Record a video of approximately five minutes demonstrating the complete prototype.
2. Upload the video to Google Drive.
3. Open the sharing settings.
4. Set general access to "Anyone with the link" with Viewer permission, if permitted by your institution.
5. Copy the shareable URL.
6. Add the URL to `submission/Video_Presentation_Link.docx`.
7. Verify that the link opens without requiring additional access approval.

### 7. Final Verification Checklist

- [ ] All three review presentations are uploaded.
- [ ] The application runs successfully.
- [ ] Database tables, relationships, and constraints are verified.
- [ ] SQL scripts are included.
- [ ] Actual application screenshots are included.
- [ ] The final report follows the prescribed format.
- [ ] The five-minute video link is publicly accessible.
- [ ] The GitHub repository is accessible to the evaluator.
- [ ] No passwords, private credentials, or real personal employee data are uploaded.

### 8. Important Notes

- Keep the README updated with setup instructions and project features.
- Ensure the SQL scripts match the database used by the application.
- Do not claim features are implemented or tested until they have been verified.
- Submit the final report's hardcopy as instructed by the faculty.

---

**Project:** Employee Attendance, Shift and Leave Management System  
**Project Type:** Database Management System (DBMS) PBL
