employees = (
    ("Priya", 28, 65000),
    ("Rahul", 32, 75000),
    ("Amit", 25, 45000),
    ("Neha", 30, 85000),
    ("Riya", 27, 55000)
)

count = 0
highest_salary = employees[0][2]
emp_name = employees[0][0]
av_salary = 0

for i in employees:
    name, age, salary = i
    print(f"{name} is {age} years old and having {salary} salary")
    if age>27:
        count += 1
    if highest_salary<salary:
        highest_salary =salary
        emp_name = name 
    av_salary += salary       
    
print("\n-----first two employees------")
print(employees[0:2]) 

print("\n-----employees older than 27------") 
print(count)

print("\n----highest salary and highest paid employee---")
print("Highest paid employee", emp_name)
print("Highest Salary: ",highest_salary)

print("\n---Average Salary is: ")
print (av_salary/len(employees)) 