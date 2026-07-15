basic_salary=float(input("Enter the basic salary: "))
allowance=basic_salary*0.2
pf=0.12*basic_salary
tax=0.10*basic_salary
gross_salary=basic_salary+allowance
net_salary=gross_salary-pf-tax
print("Net Salary: ", net_salary)
print("Basic Salary: ", basic_salary)
print("Allowance: ", allowance)
print("Provident Fund (PF): ", pf)
print("Tax: ", tax)
print("Gross Salary: ", gross_salary) 
