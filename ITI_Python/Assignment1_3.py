First_num=int(input("Please Enter Number: "))
Last_Bit=(First_num&1)<<7
First_num=First_num>>1
First_num=First_num+Last_Bit
print(First_num)