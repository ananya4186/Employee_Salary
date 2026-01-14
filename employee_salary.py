def calculate_salary():
    print("==== Employee Salary Processing ====")

    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    dept = input("Enter department: ")
    basic_salary = float(input("Enter basic salary: "))

    # Salary calculation logic
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da

    if basic_salary <= 50000:
        tax = 0
    elif basic_salary <= 80000:
        tax = gross_salary * 0.10
    else:
        tax = gross_salary * 0.20

    net_salary = gross_salary - tax

    print("\n==== Result ====")
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {emp_id}")
    print(f"Department    : {dept}")
    print(f"Basic Salary  : {basic_salary}")
    print(f"Gross Salary  : {gross_salary}")
    print(f"Net Salary    : {net_salary}")


# main execution
if __name__ == "__main__":
    calculate_salary()
