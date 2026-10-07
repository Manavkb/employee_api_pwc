"""
===============================================================================
 FASTAPI CORPORATE TRAINING
 Module 03 - Project Structure & APIRouter
 Project : Enterprise Employee Management API
===============================================================================

main.py is now SMALL. Its only jobs:
  1. create the FastAPI app
  2. define startup / shutdown behaviour (lifespan)
  3. plug in (include) the routers

HOW TO RUN - from the employee_api folder (the one that CONTAINS app/):
    pip install fastapi uvicorn
    uvicorn app.main:app --reload

    app.main  -> the file app/main.py   (folder.file, dots instead of slashes)
    :app      -> the FastAPI object inside it

OPEN:  http://127.0.0.1:8000/docs
===============================================================================
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.routers import departments, employees, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs ONCE when the server starts (connect to DB, load models, warm caches)
    print(f"Starting {settings.APP_NAME} v{settings.VERSION} [{settings.ENVIRONMENT}]")
    yield
    # Runs ONCE when the server stops (close connections, flush logs)
    print("Shutting down cleanly")


app = FastAPI(title=settings.APP_NAME, version=settings.VERSION, lifespan=lifespan)

# Plug in the routers
app.include_router(health.router)                                    # /health
app.include_router(employees.router, prefix=settings.API_PREFIX)     # /api/v1/employees
app.include_router(departments.router, prefix=settings.API_PREFIX)   # /api/v1/departments


@app.get("/", tags=["General"])
def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}", "docs": "/docs"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app = "main:app", host="127.0.0.1", port=8000, reload=True)