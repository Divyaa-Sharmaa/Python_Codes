emp_name = input("Enter your name: ")
emp_salary = float(input("Enter your salary: "))
bonus_percentage = float(input("enter your bonus percentage: "))
if emp_salary>=50000:
    bonus = emp_salary * (bonus_percentage/100)
else: 
     bonus = emp_salary * (bonus_percentage/100)  
total_sal = emp_salary + bonus  
   
print("\n----- Employee Details -----")
print(f"Employee Name: {emp_name}")
print(f"Employee Salary: {emp_salary}")
print(f"Bonus: {bonus}")
print(f"Total Salary: {total_sal}")