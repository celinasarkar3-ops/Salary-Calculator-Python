Employee = str(input("Enter Employee Name: "))
Salary = float(input("Enter your Salary: "))
Bonus = int(input("Enter your bonus Amount: "))
Tax_rate = float(input("Enter your Tax rate: "))


Gross_salary = Salary + Bonus
Tax_Amount = (Gross_salary*Tax_rate)/100
Net_Salary = Gross_salary - Tax_Amount 

print("------------------------")
print(Employee,"your Gross Salary is: ", Gross_salary)
print(Employee,"your Tax Amount is: ", Tax_Amount)
print(Employee,"your Net Salary is: ", Net_Salary)
