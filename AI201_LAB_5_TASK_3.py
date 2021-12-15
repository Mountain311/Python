data={}
record={}

def record_in():
    serial_no=input("Input Employee Serial Number : ")
    name=(input("Input Employee Name : "))
    age=(input("Input Employee Age : "))
    salary=(input("Input Employee Salary : "))
    data["Name"]=name 
    data["Age"]=age 
    data["Salary"]=salary
    record[serial_no]=data


record_in()

print(record)
