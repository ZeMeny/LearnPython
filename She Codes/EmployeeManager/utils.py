import json
import re
import datetime


class Employee:
    def __init__(self, name, emp_id, phone, age):
        self.name = name
        self.emp_id = emp_id
        self.phone = phone
        self.age = age
        self.attendance_log = []


employeeList = []


def addNewEmployee():
    name = input("enter a name: ")
    if len(name) > 40:
        raise Exception("name is too long!")
    emp_id = input("enter a valid id: ")
    if not validateID(emp_id):
        raise Exception("invalid ID!")
    phone = input("enter phone number: ")
    if not validatePhone(phone):
        raise Exception("Invalid phone number!")
    age = input("enter age: ")
    if not validateAge(age):
        raise Exception("Invalid age!")
    employeeList.append(Employee(name, emp_id, phone, age))
    print("employee added successfully")
    SaveDataFile()


def removeEmployee():
    emp_id = input("Enter the employee id you wish to remove")
    if emp_id in employeeList.count(lambda x: x.emp_id == emp_id) > 0:
        employeeList.remove(lambda x: x.emp_id == emp_id)
        SaveDataFile()
        print("employee removed successfully")
    else:
        print("Id not found")


def printAll():
    for emp in employeeList:
        print(f"{emp.name}: {emp.emp_id}")


def writeEmployee(emp, path):
    json.dump(emp, path)
    SaveDataFile()


def addMultipleEmployees():
    path = input("Enter a path to employees json file")
    f = open(path, 'r')
    employees = json.loads(f.read())
    employeeList.append(employees)
    SaveDataFile()
    print(f"{len(employees)} employees added successfully")


def removeMultipleEmployees():
    path = input("Enter a path to employees json file")
    f = open(path, 'r')
    employees = json.loads(f.read())
    employeeList.remove(employees)
    SaveDataFile()
    print(f"{len(employees)} employees removed successfully")


def markAttendance():
    user_id = input("Enter employee id")
    employeeListById = [emp for emp in employeeList if emp.emp_id == user_id]
    if len(employeeListById) > 0:
        employeeListById[0].attendance_log.append(datetime.datetime.now())
        print(f"attendance marked for {user_id} at {datetime.datetime.now()}")
    else:
        print("id not found")


def printMonthlyReport():
    # todo: implement
    pass


def printEmployeeAttendanceReport():
    # todo: implement
    pass


def printLateEmployees():
    # todo: implement
    pass


def SaveDataFile():
    with open('EmployeeListData.json', 'r+') as outfile:
        json.dump(employeeList, outfile, indent=4)


def validateID(emp_id):
    valid = emp_id.isnumeric()
    valid = valid and emp_id not in employeeList
    return valid


def validatePhone(phone):
    valid = phone.isnumeric()
    pattern = "(\w{3})\w{3}-\w{4}"  # todo: find a pattern
    valid = valid and re.search(pattern, phone)
    return valid


def validateAge(age):
    valid = age.isnumeric()
    valid = valid and int(age) in range(18, 100)
    return valid
