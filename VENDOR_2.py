#Construct a program to store the following details of a Vendor of a Shop. a) Name of vendor, b) Year of association ,c) Contact number ,d) eMail ID ,Read the details of monthly purchases from Vendor and generate a Annual Purchase/Billing report.
vendor_name = input("Enter vendor name: ")
year_of_association = int(input("Enter year of association: "))
contact_number = input("Enter contact number: ")
email_id = input("Enter email id: ")

total_purchase = 0

for i in range(12):
    amount = float(input("Enter monthly purchase: "))
    total_purchase = total_purchase + amount

print("Vendor Name:", vendor_name)
print("Year of Association:", year_of_association)
print("Contact Number:", contact_number)
print("Email ID:", email_id)
print("Annual Purchase:", total_purchase)