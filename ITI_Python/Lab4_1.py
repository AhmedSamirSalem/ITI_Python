print('''
|*************************************|
|To Add New Item Press 1              |
|To Print The TO Do List Press 2      |
|To Mark an item as Done Press 3      |
|To Print the done list  Press 4      |
|*************************************|
''')

To_Do_List=[]
Done_List=[]
while True:
    Option = int(input("Please enter yout choice: "))
    if Option == 1:
        To_Do_List.append(input("Enter Task: "))
    elif Option == 2:
        print(To_Do_List)
    elif Option == 3:
        Task=input("Enter Task: ")
        if Task in  To_Do_List:
            Done_List.append(Task)
            To_Do_List.d(Task)
        elif To_Do_List[int(Task)-1]  in  To_Do_List :
            Done_List.append(To_Do_List[int(Task)-1])
            To_Do_List.remove(To_Do_List[int(Task)-1])
        else:
            print("Task does not Exist")
    elif Option == 4:
        print(Done_List)
    else:
        print("Invaild Option")