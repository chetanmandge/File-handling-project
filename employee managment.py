import os
def add_employee():
    with open("employee_db.text","a") as fp:
        name=input("enter employee name:-")
        Eid=input("enter employee ID :-")
        dept = input(" enter employee department :-")
        fp.write(f"{name}~{Eid}~{dept}~\n")
        print(f"employee {name} added successfully")

add_employee()