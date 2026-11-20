#Function 1
def add_employee(employee_name,employee_id,salary):
    f = open("employees.txt", "a" )
    f.write(employee_name +"|"+ employee_id +"|"+ salary+ "\n") # Rahim|E101|25000
    f.close()
    return "Employee Added Successfully"

#function 2
def view_employees():
    f = open("employees.txt", "r")
    data = f.read()
    f.close()

    if data == "":
        print("No Employee information")
    else:
        print("Employee information")
        print(data)

while True:
    print("1. Add_Employee")
    print("2. View_Employees")
    print("3. Exit")

    choose = input("Choose option: ")

    if choose == "1":
        employee_name = input("Enter Name: ")
        employee_id = input("Enter ID: ")
        salary = input("Enter Salary: ")

        print(add_employee(employee_name, employee_id, salary))

    elif choose == "2":
        view_employees()

    elif choose == "3":
        print("Exit")
        break

    else:
        print("Try again")
