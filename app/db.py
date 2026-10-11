import sqlite3
from pathlib import Path
from flask import current_app, g

def get_db():
    if "db" not in g:
        db_path = current_app.config["DATABASE"]
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.executescript("""
    CREATE TABLE IF NOT EXISTS employees (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      code TEXT NOT NULL UNIQUE,
      full_name TEXT NOT NULL,
      email TEXT NOT NULL,
      department TEXT NOT NULL,
      hire_date TEXT NOT NULL,
      active INTEGER NOT NULL DEFAULT 1
    );
    CREATE TABLE IF NOT EXISTS shifts (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      start_time TEXT NOT NULL,
      end_time TEXT NOT NULL,
      break_minutes INTEGER NOT NULL DEFAULT 30 CHECK (break_minutes >= 0)
    );
    CREATE TABLE IF NOT EXISTS attendance (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      employee_id INTEGER NOT NULL REFERENCES employees(id),
      work_date TEXT NOT NULL,
      clock_in TEXT NOT NULL,
      clock_out TEXT,
      status TEXT NOT NULL CHECK (status IN ('Present','Absent','Late')),
      UNIQUE(employee_id, work_date),
      CHECK (clock_out IS NULL OR clock_out > clock_in)
    );
    CREATE TABLE IF NOT EXISTS leave_requests (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      employee_id INTEGER NOT NULL REFERENCES employees(id),
      leave_type TEXT NOT NULL,
      start_date TEXT NOT NULL,
      end_date TEXT NOT NULL,
      reason TEXT NOT NULL,
      status TEXT NOT NULL DEFAULT 'Pending'
        CHECK (status IN ('Pending','Approved','Rejected')),
      CHECK (end_date >= start_date)
    );
    """)
    if db.execute("SELECT COUNT(*) FROM employees").fetchone()[0] == 0:
        db.executemany("""INSERT INTO employees
          (code, full_name, email, department, hire_date) VALUES (?,?,?,?,?)""", [
          ("EMP001","Aarav Sharma","aarav@example.com","Engineering","2025-06-01"),
          ("EMP002","Diya Reddy","diya@example.com","Engineering","2025-08-15"),
          ("EMP003","Kabir Rao","kabir@example.com","Engineering","2026-01-10"),
          ("EMP004","Ravi krishna","ravikrishna12@gmail.com","Administration","2026-10-10")
        ])
    if db.execute("SELECT COUNT(*) FROM shifts").fetchone()[0] == 0:
        db.executemany("INSERT INTO shifts (name,start_time,end_time,break_minutes) VALUES (?,?,?,?)", [
          ("Morning","09:00","17:00",30), ("Evening","13:00","21:00",30), ("Night","21:00","05:00",30)
        ])
    if db.execute("SELECT COUNT(*) FROM attendance").fetchone()[0] == 0:
        db.executemany("""INSERT INTO attendance
          (employee_id,work_date,clock_in,clock_out,status) VALUES (?,?,?,?,?)""", [
          (4,"2026-10-10","09:00",None,"Absent"),
          (2,"2026-10-10","09:00",None,"Present"),
          (3,"2026-10-10","09:00",None,"Present"),
          (1,"2026-10-10","09:00",None,"Present")
        ])
    if db.execute("SELECT COUNT(*) FROM leave_requests").fetchone()[0] == 0:
        db.execute("""INSERT INTO leave_requests
          (employee_id,leave_type,start_date,end_date,reason,status)
          VALUES (1,'Casual Leave','2026-10-10','2026-10-10','had a function','Approved')""")
    db.commit()
