#Construct a program to store the information of an employee such as name, employee ID, department and generate the salary as per the following conditions:(i) DA is 92% of Basic Salary,(ii) HRA is 58% of Basic Salary,(iii) TA is 30% of Basic Salary,(iv) LIC is deducted: Rs. 500 every month.
name = input("Enter Employee Name: ")
eid = input("Enter Employee ID: ")
department = input("Enter Department: ")
basicsalary = float(input("Enter Basic Salary: "))
da = 0.92 * basicsalary
hra = 0.58 * basicsalary
ta = 0.30 * basicsalary
lic = 500
grosssalary = basicsalary + da + hra + ta
netsalary = grosssalary - lic
print("Employee Salary Details ")
print("Name:", name)
print("Employee ID:", eid)
print("Department:", department)
print("Basic Salary:", basicsalary)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction:", lic)
print("Net Salary:", netsalary)