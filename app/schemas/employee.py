"""
schemas/employee.py - Pydantic models (the data contracts from Module 02).

Schemas describe WHAT data looks like. They know nothing about routes.
"""
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Department(str, Enum):
    ENGINEERING = "Engineering"
    HR = "HR"
    FINANCE = "Finance"
    SALES = "Sales"


class EmployeeCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=2, max_length=50, examples=["Karan Shah"])
    department: Department
    role: str = Field(min_length=2, max_length=60, examples=["Account Executive"])
    location: str = "Bengaluru"


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: Department
    role: str
    location: str


class DepartmentSummary(BaseModel):
    department: Department
    headcount: int
