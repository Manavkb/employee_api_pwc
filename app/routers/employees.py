"""
routers/employees.py - every endpoint about employees.

APIRouter works exactly like `app`, but it is a SEPARATE, smaller group.
prefix="/employees" is added in front of every path in this file.
main.py later adds "/api/v1" in front of that.

    @router.get("/{employee_id}")  ->  /api/v1/employees/{employee_id}
"""
from fastapi import APIRouter, HTTPException, status

from app.schemas.employee import Department, EmployeeCreate, EmployeeResponse
from app.services import employee_service

from typing import Optional
router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("", response_model=list[EmployeeResponse])
def list_employees(department: Optional[Department]  = None):
    """GET /api/v1/employees  (optional ?department=HR)"""
    return employee_service.list_employees(department)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):
    """GET /api/v1/employees/101"""
    employee = employee_service.get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")
    return employee


@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(payload: EmployeeCreate):
    """POST /api/v1/employees"""
    return employee_service.create_employee(payload)
