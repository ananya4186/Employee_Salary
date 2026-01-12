import os

def calculate_salary(basic_salary):
    if basic_salary <= 0:
        return -1, -1

    hra = 0.20 * basic_salary
    da = 0.10 * basic_salary
    gross_salary = basic_salary + hra + da

    if gross_salary > 80000:
        tax = 0.20 * gross_salary
    elif gross_salary >= 50000:
        tax = 0.10 * gross_salary
    else:
        tax = 0

    net_salary = gross_salary - tax
    return gross_salary, net_salary


if __name__ == "__main__":
    emp_name = os.getenv("EMP_NAME", "Employee")
    emp_id = os.getenv("EMP_ID", "E001")
    department = os.getenv("DEPARTMENT", "IT")
    basic_salary = float(os.getenv("BASIC_SALARY", "30000"))

    gross, net = calculate_salary(basic_salary)

    print("=== Employee Salary Management System ===")
    print("Employee Name :", emp_name)
    print("Employee ID   :", emp_id)
    print("Department    :", department)
    print("Basic Salary  :", basic_salary)

    if gross == -1:
        print("Invalid Salary")
    else:
        print("Gross Salary  :", gross)
        print("Net Salary    :", net)
