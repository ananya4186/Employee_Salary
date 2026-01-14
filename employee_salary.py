import sys

def calculate_salary(name, emp_id, dept, basic_salary):
    print("==== Employee Salary Processing ====")

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


if __name__ == "__main__":
    # Jenkins / Docker (non-interactive)
    if len(sys.argv) == 5:
        name = sys.argv[1]
        emp_id = sys.argv[2]
        dept = sys.argv[3]
        salary = float(sys.argv[4])
    else:
        # Local / interactive
        print("==== Employee Salary Processing ====")
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        dept = input("Enter department: ")
        salary = float(input("Enter basic salary: "))

    calculate_salary(name, emp_id, dept, salary)
