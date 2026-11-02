print("----write to the file----") 
with open("employees.txt","w") as file:
    file.write("Priya,65000\n")
    file.write("Rahul,45000\n")
    file.write("Neha,85000")

print("----read----") 
with open("employees.txt", "r") as file:
    content = file.read()
    print(content)
    
print("----readline----") 
with open("employees.txt", "r") as file:
    print(file.readline())
    print(file.readline())  
    
print("----read employees records line by line-----")
with open("employees.txt", "r") as file:
    content = file.readline()
    while content!="":
       print(content)
       content = file.readline()

print("--add an employee---")  
with open("employees.txt","a") as file:
    content = file.write("\nAmit,55000") 

print("----convert file data into objects----") 
with open("employees.txt", "r") as file:
    content = file.readline()
    emp = []
    total = 0
    while content!="":
        result = content.strip().split(",")
        print(result)
        sal = int(result[1])
        
        emp.append({
            "name" : result[0],
            "salary" : sal
        })
        content = file.readline()
    print(emp) 
    emp_name = emp[0]["name"] 
    high_sal = emp[0]["salary"]
    count = 0
    for e in emp:
        sal = e.get("salary")
        total += sal
        if high_sal<sal:
            high_sal = sal
            emp_name = e.get("name")
        if sal>60000:
            count += 1    
    print("total salary: ", total) 
    print("average sal: ", total/len(emp))
    print("highest paid emp:",emp_name, " and highest salary is: ",high_sal) 
    print("count: ",count)  
          
    
                       