employee = []
while True:
    Employee = str(input("Enter Employee Name: "))
    Salary = float(input("Enter your Salary: "))
    Bonus = int(input("Enter your bonus Amount: "))
    Tax_rate = float(input("Enter your Tax rate: "))

    if Salary < 0 or Bonus < 0 :
        print("Invalid Input! Salary and Bonus must be non-negative.")
        continue


    Gross_salary = Salary + Bonus
    Tax_Amount = (Gross_salary*Tax_rate)/100
    Net_Salary = Gross_salary - Tax_Amount 

    employee.append([Employee, Salary, Bonus, Tax_rate, Gross_salary, Tax_Amount, Net_Salary])
    
    print("------------------------")
    print(f'{Employee} Salary Details:')
    print(f"Gross Salary: {Gross_salary}")
    print(f"Tax Amount: {Tax_Amount}")
    print(f"Net Salary: {Net_Salary}")


    choice = input("Do you want to add another employee? (yes/no): ").strip().lower()
    if choice != 'yes':
        break
print("\nSummary of all employees:" , employee)