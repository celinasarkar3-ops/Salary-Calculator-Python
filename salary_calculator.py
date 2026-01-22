# Salary Calculator
# This program calculates the gross salary, tax amount, and net salary for employees based on user input.
# Author: celina sarkar

Employee = []
def add_employee():
    name  = str(input("Enter Employee Name: "))
    Salary = float(input("Enter your Salary: "))
    Bonus = float(input("Enter your bonus Amount: "))
    Tax_rate = float(input("Enter your Tax rate(%): "))

    if Salary < 0 or Bonus < 0 or Tax_rate < 0:
        print("Invalid Input! Salary, Bonus and tax rate must be non-negative.")
        return

    Gross_salary = Salary + Bonus
    Tax_Amount = (Gross_salary*Tax_rate)/100
    Net_Salary = Gross_salary - Tax_Amount 

    employee = {
        'Name': name,
        'Gross Salary': Gross_salary,
        'Tax Amount': Tax_Amount,
        'Net Salary': Net_Salary
    }
    Employee.append(employee)

    print("\n------------------------")
    print("Employee Salary Details")
    print("------------------------\n")
    print(f'Name         : {name}')
    print(f"Gross Salary : {Gross_salary:.2f}")
    print(f"Tax Amount   : {Tax_Amount:.2f}")
    print(f"Net Salary   : {Net_Salary:.2f}")

print("------------------------\n")
def view_employees():
    if not Employee:
        print("No employees added yet.")
        return
    print("\n ========== All Employees ==========")
    for i in Employee:
        print(f"Name: {i['Name']}, Gross Salary: {i['Gross Salary']:.2f}, Tax Amount: {i['Tax Amount']:.2f}, Net Salary: {i['Net Salary']:.2f}")
def highest_net_salary():
    if not Employee:
        print("No employees added yet.")
        return
    highest = Employee[0]
    for emp in Employee:
        if emp['Net Salary'] > highest['Net Salary']:
            highest = emp
    print("\n🏆Employee with the highest Net Salary: ")        
    print(f"Name: {highest['Name']}, Gross Salary: {highest['Gross Salary']:.2f}, Tax Amount: {highest['Tax Amount']:.2f}, Net Salary: {highest['Net Salary']:.2f}")
    print("------------------------\n")
       
def summary_report():
    if not Employee:
        print("No employees added yet.")
        return
    total = 0
    for emp in Employee:
        total += emp['Net Salary']
    average = total / len(Employee)
    print("\n===== Summary Report =====")
    print(f"Total Employees: {len(Employee)}")
    print(f"Average Net Salary: {average:.2f}")
    print("------------------------\n")
#----- Main Menu------
while True:
    print("===== Salary Calculator Menu =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Employee with Highest Net Salary")
    print("4. Summary Report")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        highest_net_salary()
    elif choice == '4':
        summary_report()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
    print("------------------------\n")
   

