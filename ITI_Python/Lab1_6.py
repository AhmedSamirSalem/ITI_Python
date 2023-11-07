Customer_Name = input("Please Enter Customer Name: ")
Shopping_amount = input("Please Enter Shopping amount : ")
Discount_Precentage = int(input("Please Enter Discount Precentage : "))

discount=int(Shopping_amount)-(int(Shopping_amount)*Discount_Precentage/100)
print("Dear"+ Customer_Name+"\n")
print("Thank You For Shooping\n")
print("Total Amout is\n"+Shopping_amount)
print("you got "+str(Discount_Precentage)+"%")
print("Total Value After discount: "+str(discount))

