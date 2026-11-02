employees = [
    {"name": "Priya", "salary": 65000, "department": "IT"},
    {"name": "Rahul", "salary": 45000, "department": "HR"},
    {"name": "Neha", "salary": 85000, "department": "IT"}
]

total = 0 
highest_salary = employees[0]["salary"]
emp_name = employees[0]["name"]
count = 0 
new_sal = 0

for emp in employees:
    print(emp.get("name"), emp.get("salary"))
    total += emp.get("salary")
    if highest_salary<emp.get("salary"):
            highest_salary = emp.get("salary")
            emp_name = emp.get("name") 
    if emp.get("department")=="IT":
        count += 1  
        
print("total salary: ",total)
print("highest paid employee name: ", emp_name)
print("IT employee count: " , count)                  

for emp in employees:
    if emp.get("name")=="Rahul":
            curr_sal = emp.get("salary")
            inc = curr_sal*0.1
            new_sal = curr_sal+inc
            emp["salary"] = new_sal
print(f"Rahul's new salary: {new_sal}")

#add employee
employees.append({"name": "Amit","salary": 55000,"department": "Finance"}) 

for emp in employees:
    print(emp)
  
    