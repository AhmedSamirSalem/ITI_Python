print('''
|*************************************|
|To Add New Employee     Press 1      |
|To Print Employee Data  Press 2      |
|To Delete Employee      Press 3      |
|*************************************|
''')

Employee_Data={}
while True:
    Option = int(input("Please enter your choice: "))
    if Option == 1:
        Employee_Id=int(input("Please enter Employee id: "))
        if Employee_Id in Employee_Data:
            print("Employee id is exist Please enter unique id")
        else :
            Name=input("Please Enter Employee Name: ")
            Job=input("Please Enter Employee Job: ")
            Salary=float(input("Please Enter Employee Salary: "))
            Employee_Data[Employee_Id]={"Name":Name,"Job":Job,"Salary":Salary}
    elif Option == 2:
        Employee_Id=int(input("Please enter Employee id: "))
        if Employee_Id in Employee_Data:
            print(Employee_Data[Employee_Id])
        else:
            print("Employee id is not exist Please enter Valid id")
    elif Option == 3:
        Employee_Id=int(input("Please enter Employee id: "))
        if Employee_Id in Employee_Data:
            Employee_Data.pop(Employee_Id)
        else:
            print("Employee id is not exist Please enter Valid id")
    else:
        print("Invaild Option")