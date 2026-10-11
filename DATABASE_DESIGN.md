
# DATABASE DESIGN
## Employee Attendance, Shift and Leave Management System

### 1. Overview
The system uses a relational database to manage employee details, departments, shifts, rosters, attendance records, leave types, leave balances, and leave requests.

### 2. Database Tables

1. **Departments** — Stores department details.
2. **Employees** — Stores employee information and department assignment.
3. **Shifts** — Stores shift names, start times, end times, and break durations.
4. **Rosters** — Assigns employees to shifts on specific dates.
5. **Attendance** — Stores daily clock-in, clock-out, and attendance status.
6. **Leave_Types** — Stores leave categories and annual entitlements.
7. **Leave_Balances** — Tracks entitled, used, and available leave for each employee and year.
8. **Leave_Requests** — Stores leave applications, dates, reasons, and approval status.

### 3. Primary Keys and Foreign Keys

- Departments: `id` is the primary key.
- Employees: `id` is the primary key; `department_id` references Departments.
- Shifts: `id` is the primary key.
- Rosters: `id` is the primary key; `employee_id` references Employees and `shift_id` references Shifts.
- Attendance: `id` is the primary key; `employee_id` references Employees.
- Leave_Types: `id` is the primary key.
- Leave_Balances: composite primary key `(employee_id, leave_type_id, year)`.
- Leave_Requests: `id` is the primary key; `employee_id` references Employees and `leave_type_id` references Leave_Types.

### 4. Integrity Constraints

- Employee codes and email addresses must be unique.
- Required fields cannot be NULL.
- One attendance record per employee per date.
- One roster assignment per employee per date.
- Clock-out must be later than clock-in for the same-day attendance rule.
- Leave dates must be valid and the end date cannot precede the start date.
- Leave balances cannot be negative or exceed entitled days.
- Leave request status must be Pending, Approved, or Rejected.

### 5. Normalization

The design separates departments, employees, shifts, attendance, and leave information into related tables to reduce duplication and update anomalies. Primary keys identify records, and foreign keys maintain referential integrity. The final functional dependencies and 1NF, 2NF, and 3NF analysis should be verified against the implemented schema.

### 6. Database Implementation

The starter prototype uses SQLite. The schema is available in `sql/schema_sqlite.sql`. A MySQL-compatible schema can be maintained separately if required.
