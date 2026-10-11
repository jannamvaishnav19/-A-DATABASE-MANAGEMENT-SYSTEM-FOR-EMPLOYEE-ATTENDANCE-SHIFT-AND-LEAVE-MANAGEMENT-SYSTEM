from datetime import date
from flask import Blueprint, flash, redirect, render_template, request, url_for
from .db import get_db

bp = Blueprint("main", __name__)

@bp.app_context_processor
def inject_today():
    return {"today": date.today().isoformat()}

@bp.route("/")
def dashboard():
    db = get_db()
    stats = {
      "employees": db.execute("SELECT COUNT(*) FROM employees WHERE active=1").fetchone()[0],
      "attendance": db.execute("SELECT COUNT(*) FROM attendance WHERE work_date=?", (date.today().isoformat(),)).fetchone()[0],
      "pending": db.execute("SELECT COUNT(*) FROM leave_requests WHERE status='Pending'").fetchone()[0],
      "shifts": db.execute("SELECT COUNT(*) FROM shifts").fetchone()[0]
    }
    recent = db.execute("""SELECT a.*, e.code, e.full_name FROM attendance a
      JOIN employees e ON e.id=a.employee_id ORDER BY a.work_date DESC,a.id DESC LIMIT 8""").fetchall()
    return render_template("dashboard.html", stats=stats, recent=recent)

@bp.route("/employees", methods=["GET","POST"])
def employees():
    db = get_db()
    if request.method == "POST":
        try:
            db.execute("""INSERT INTO employees(code,full_name,email,department,hire_date)
              VALUES(?,?,?,?,?)""", (request.form["code"].strip(), request.form["full_name"].strip(),
              request.form["email"].strip(), request.form["department"], request.form["hire_date"]))
            db.commit()
            flash("Employee added successfully.", "success")
        except Exception as exc:
            db.rollback()
            flash(f"Could not add employee: {exc}", "error")
        return redirect(url_for("main.employees"))
    rows = db.execute("SELECT * FROM employees ORDER BY code").fetchall()
    return render_template("employees.html", employees=rows)

@bp.route("/shifts", methods=["GET","POST"])
def shifts():
    db = get_db()
    if request.method == "POST":
        try:
            db.execute("INSERT INTO shifts(name,start_time,end_time,break_minutes) VALUES(?,?,?,?)",
              (request.form["name"].strip(),request.form["start_time"],request.form["end_time"],int(request.form["break_minutes"])))
            db.commit()
            flash("Shift created successfully.", "success")
        except Exception as exc:
            db.rollback()
            flash(f"Could not create shift: {exc}", "error")
        return redirect(url_for("main.shifts"))
    rows = db.execute("SELECT * FROM shifts ORDER BY id").fetchall()
    return render_template("shifts.html", shifts=rows)

@bp.route("/attendance", methods=["GET","POST"])
def attendance():
    db = get_db()
    if request.method == "POST":
        try:
            db.execute("""INSERT INTO attendance(employee_id,work_date,clock_in,clock_out,status)
              VALUES(?,?,?,?,?) ON CONFLICT(employee_id,work_date) DO UPDATE SET
              clock_in=excluded.clock_in, clock_out=excluded.clock_out, status=excluded.status""",
              (int(request.form["employee_id"]),request.form["work_date"],request.form["clock_in"],
               request.form.get("clock_out") or None,request.form["status"]))
            db.commit()
            flash("Attendance saved successfully.", "success")
        except Exception as exc:
            db.rollback()
            flash(f"Could not save attendance: {exc}", "error")
        return redirect(url_for("main.attendance"))
    employees = db.execute("SELECT id,code,full_name FROM employees WHERE active=1 ORDER BY code").fetchall()
    rows = db.execute("""SELECT a.*,e.code,e.full_name FROM attendance a JOIN employees e ON e.id=a.employee_id
      ORDER BY a.work_date DESC,a.id DESC LIMIT 100""").fetchall()
    return render_template("attendance.html", employees=employees, records=rows)

@bp.route("/leave", methods=["GET","POST"])
def leave():
    db = get_db()
    if request.method == "POST":
        try:
            db.execute("""INSERT INTO leave_requests(employee_id,leave_type,start_date,end_date,reason)
              VALUES(?,?,?,?,?)""", (int(request.form["employee_id"]),request.form["leave_type"],
              request.form["start_date"],request.form["end_date"],request.form["reason"].strip()))
            db.commit()
            flash("Leave request submitted.", "success")
        except Exception as exc:
            db.rollback()
            flash(f"Could not submit request: {exc}", "error")
        return redirect(url_for("main.leave"))
    employees = db.execute("SELECT id,code,full_name FROM employees WHERE active=1 ORDER BY code").fetchall()
    rows = db.execute("""SELECT l.*,e.code,e.full_name FROM leave_requests l
      JOIN employees e ON e.id=l.employee_id ORDER BY l.id DESC""").fetchall()
    return render_template("leave.html", employees=employees, requests=rows)

@bp.post("/leave/<int:request_id>/<decision>")
def decide_leave(request_id, decision):
    if decision not in ("Approved","Rejected"):
        flash("Invalid decision.", "error")
        return redirect(url_for("main.leave"))
    db = get_db()
    db.execute("UPDATE leave_requests SET status=? WHERE id=? AND status='Pending'", (decision,request_id))
    db.commit()
    flash(f"Leave request marked {decision.lower()}.", "success")
    return redirect(url_for("main.leave"))

@bp.route("/reports")
def reports():
    db = get_db()
    summary = db.execute("""SELECT substr(work_date,1,7) AS month,status,COUNT(*) AS records
      FROM attendance GROUP BY substr(work_date,1,7),status ORDER BY month DESC,status""").fetchall()
    leave_rows = db.execute("""SELECT e.code,e.full_name,l.leave_type,
      COUNT(*) AS requests, SUM(CASE WHEN l.status='Approved' THEN 1 ELSE 0 END) AS approved
      FROM employees e LEFT JOIN leave_requests l ON l.employee_id=e.id
      GROUP BY e.id,l.leave_type ORDER BY e.code""").fetchall()
    return render_template("reports.html", summary=summary, leave_rows=leave_rows)
