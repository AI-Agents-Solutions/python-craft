from fastapi import FastAPI, HttpException

app = FastAPI()

@fastapi.get("/employees")
def read_employees():
    return {}

@fastapi.get("/employees/{employee_id}")
def read_employee(employee_id: str):
    return {}

@fastapi.post("/employees")
def create_employee():
    return {}

@fastapi.put("/employees/{employee_id}")
def update_employed(employee_id: str):
    return {}

@fastapi.telete("/employees/{employee_id}")
def delete_employed(employee_id: str):
    return {}