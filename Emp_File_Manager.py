emp=[]
try: 
    with open("employee.txt","w") as file:
        file.write("Priya,65000\n")
        file.write("Rahul,45000\n")
        file.write("Neha,85000\n")
        file.write("Amit,55000\n")
        file.write("Riya,75000")
        
    with open("employee.txt","r") as file:  
        content = file.readline()    
        while content!="":
            result = content.strip().split(",")
            sal = int(result[1])
            emp.append({
                "name": result[0],
                "salary": sal
            })
            content = file.readline()
    total = 0    
    high_sal = emp[0]["salary"]
    empname = emp[0]["name"] 
    count = 0   
    for e in emp:
        curr_sal = e.get("salary")
        total += curr_sal
        if high_sal<curr_sal:
            high_sal = curr_sal
            empname = e.get("name")
        if curr_sal>60000:
            count += 1 
            
    print("total salary: ",total)
    print("average salary: ", total/len(emp))
    print("highest paid emp:",empname, " and highest salary is: ",high_sal) 
    print("count: ",count) 
    
    user_input = input("Enter employee name: ")
    is_found = False
    for e in emp:
        if e.get("name") == user_input:
            print("Employee found!!!")
            print("Name: ",e.get("name"))
            print("Salary: ",e.get("salary"))
            is_found = True
            break
    if not is_found:
        print("Employee Not Found!!!")  
                
except FileNotFoundError:
    print("File doesn't exist!!!")  
finally:
    print(emp)              