"""
data/database.py - where data lives.

Today: an in-memory dictionary.
Later: a real database. Only THIS file (and the service) will need to change.
"""
EMPLOYEES: dict[int, dict] = {
    101: {"id": 101, "name": "Asha Rao", "department": "Engineering",
          "role": "Backend Developer", "location": "Bengaluru"},
    102: {"id": 102, "name": "Priya Nair", "department": "HR",
          "role": "HR Business Partner", "location": "Chennai"},
    103: {"id": 103, "name": "Rahul Mehta", "department": "Engineering",
          "role": "Data Engineer", "location": "Pune"},
    104: {"id": 104, "name": "Vikram Singh", "department": "Finance",
          "role": "Financial Analyst", "location": "Mumbai"},
}
