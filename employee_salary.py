import sys

print("==== Employee Salary Processing ====")

name = sys.argv[1]
emp_id = sys.argv[2]
dept = sys.argv[3]
s1 = int(sys.argv[4])
s2 = int(sys.argv[5])
s3 = int(sys.argv[6])

avg = (s1 + s2 + s3) / 3

print("Employee Name :", name)
print("Employee ID   :", emp_id)
print("Department    :", dept)
print("Average Score :", avg)
