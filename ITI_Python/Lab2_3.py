Phone_number=input("Please Enter Phone Number:")
Length=len(Phone_number)
if Length!=11:
    print("incomplete phonne number")
elif  Phone_number.isdigit():
    print("Phone number accepted ")
else:
    print("Phone number must contain only numbers")
    
    
 # (Phone_number==Phone_number.upper()) and (Phone_number==Phone_number.lower())