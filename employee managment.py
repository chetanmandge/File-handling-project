import os
def add_employee():
    with open("employee_db.text" , "a") as fp:
        name = input("enter employee name:-")
        Eid = input("enter employee ID :-")
        dept = input("enter employee department :-")
        fp.write(f"{name}~{Eid}~{dept}~\n")
        print(f"employee {name} added successfully")
def search_employee_byID():
    with open("employee_db.text") as fp:
        eid = input("enter employee ID you want to search :-")
        data = fp.read()
        if(data.split("~")[1]==eid):
            print(data.split("~")[0])
def listof_employee():
    with open("employee_db.text") as fp:
        for line in fp.readlines():
            print(f"name is {line.split('~')[0]} employee ID is {line.split('~')[1]} Department is {line.split('~')[2]}")
def update_employee_byID():
    with open("employee_db.text") as fp_read ,open("dummy.text" , "w") as fp_write  :
        eid = input("enter employee ID you want to update :-")
        s = " "
        while s:
            s = fp_read.readline()
            if len(s.split("~")) > 3:
                if eid == s.split("~")[1]:
                    name = input("enter employee name:-")
                    dept = input("enter employee department :-")
                    fp_write.write(f"{name}~{eid}~{dept}~\n")
                    print(f"employee {name} Updated successfully")
                else:
                    fp_write.write(s)
    os.remove("employee_db.text")
    os.rename("dummy.text", "employee_db.text")
def delete_employee():
    with open("employee_db.text") as fp_read,open("dummy.text", "w") as fp_write:
        eid = input("enter employee ID you want to Delete :-")
        s = " "
        while s:
            s = fp_read.readline()
            if len(s.split("~")) > 3:
                if eid == s.split("~")[1]:
                    pass
                else:
                    fp_write.write(s)
    os.remove("employee_db.text")
    os.rename("dummy.text", "employee_db.text")

# add_employee()
# search_employee_byID()
# listof_employee()
# update_employee_byID()
# delete_employee()
while True:

    print("""
                ***************** Employee Managment system *****************
                                  1 : Add employee
                                  2 : update 
                                  3 : search by id
                                  4 : search all employee
                                  5 : Delete Student
                                  6 : EXIT
    """)

    ch = input("Enter Your Choice: ")

    if ch == '1':
        add_employee()

    elif ch == '2':
        update_employee_byID()

    elif ch == "3":
        search_employee_byID()

    elif ch == '4':
        listof_employee()

    elif ch == '5':
        delete_employee()

    elif ch == "6":
        break