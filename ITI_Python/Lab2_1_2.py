Counter=0;
while Counter < 3 :
    User_Name=input("Please Enter user name: ")
    if User_Name=="Ahmed" :
        Password=input("Please Enter Password: ")
        if Password=="1234" :
            print("Welcome Back "+ User_Name)
            break
        else :
            print("Wrong Password")
    elif User_Name=="Ali" :
        Password=input("Please Enter Password: ")
        if Password=="6078" :
            print("Welcome Back "+ User_Name)
            break
        else :
            print("Wrong Password")
    elif User_Name=="Amr" :
        Password=input("Please Enter Password: ")
        if Password=="9345" :
            print("Welcome Back "+ User_Name)
            break
        else :
            print("Wrong Password")
    else:
        print("Wrong Username")
    Counter+=1