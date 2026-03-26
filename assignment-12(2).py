# Create a program that reads "employee.xlsx" file of Infosys Software Solutions which includes columns such as:

# Employee ID
# Employee Name
# Department
# Designation etc.

# Construct a program to print the following reports:

# a) Print the list of employees working for "Automotive" domain.
import pandas as pd
df_employee = pd.read_excel('employeee.xlsx')
automotive_employees = df_employee[df_employee['Domain'] == 'Automotive']
print("Employees working in Automotive domain:")
print(automotive_employees[['Employee ID', 'Employee Name', 'Department', 'Designation']])
# b) Print the details of an employee with employee ID given by an end user.
import pandas as pd
df_employee = pd.read_excel('employeee.xlsx')
automotive_employees = df_employee[df_employee['Domain'] == 'Automotive']
print("Employees working in Automotive domain:")
print(automotive_employees[['Employee ID', 'Employee Name', 'Department', 'Designation']])
# c) Print the list of all the Developers of Infosys.
import pandas as pd
df_employee = pd.read_excel('employeee.xlsx')
developers = df_employee[df_employee['Designation'].str.contains('Developer', case=False, na=False)]
print("List of all Developers:")
print(developers[['Employee ID', 'Employee Name', 'Department', 'Designation']])