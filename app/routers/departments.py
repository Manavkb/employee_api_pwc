"""routers/departments.py - every endpoint about departments."""
from fastapi import APIRouter

from app.schemas.employee import DepartmentSummary
from app.services import employee_service

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get("/summary", response_model=list[DepartmentSummary])
def get_department_summary():
    """GET /api/v1/departments/summary"""
    return employee_service.department_summary()
