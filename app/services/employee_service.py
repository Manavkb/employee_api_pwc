"""
services/employee_service.py - business logic.

WHY : Routers should stay thin: receive request -> call service -> return.
      Logic here can be reused by other routers, scripts and tests.
RULE: Services never import FastAPI routers. They return data or None.
"""
from app.data.database import EMPLOYEES
from app.schemas.employee import Department, EmployeeCreate
from typing import Optional

def list_employees(department: Optional[Department] = None) -> list[dict]:
    employees = list(EMPLOYEES.values())
    if department is not None:
        employees = [e for e in employees if e["department"] == department.value]
    return employees


def get_employee(employee_id: int) -> Optional[dict] :
    return EMPLOYEES.get(employee_id)


def create_employee(data: EmployeeCreate) -> dict:
    new_id = max(EMPLOYEES, default=100) + 1
    employee = {"id": new_id, **data.model_dump(mode="json")}
    EMPLOYEES[new_id] = employee
    return employee


def department_summary() -> list[dict]:
    return [
        {"department": dept.value,
         "headcount": sum(1 for e in EMPLOYEES.values() if e["department"] == dept.value)}
        for dept in Department
    ]
