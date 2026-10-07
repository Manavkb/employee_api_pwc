Enterprise Employee Management API - Module 03

Project layout
--------------
employee_api/
  app/
    main.py               create app, lifespan, include routers
    core/config.py        settings
    routers/              one file per business area (URLs live here)
    schemas/              Pydantic models
    services/             business logic
    data/                 data storage (in-memory for now)
  requirements.txt

Run (from THIS folder)
----------------------
  python -m venv venv
  venv\Scripts\activate            (Windows)   |   source venv/bin/activate  (macOS/Linux)
  pip install -r requirements.txt
  uvicorn app.main:app --reload

Open
----
  http://127.0.0.1:8000/docs
  http://127.0.0.1:8000/health
  http://127.0.0.1:8000/api/v1/employees
  http://127.0.0.1:8000/api/v1/employees/101
  http://127.0.0.1:8000/api/v1/departments/summary
