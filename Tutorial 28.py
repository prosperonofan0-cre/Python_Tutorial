
file_path = "/storage/emulated/0/Download/employees.txt"

employee_file = open(file_path, "r")
for employee in employee_file.readlines():
    print(employee)
print(employee_file.readlines())
employee_file.close()
