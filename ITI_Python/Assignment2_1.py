sum1=0
max1=0
min1=0
counter = 0
while counter < 10:
    Number = int(input("Please Enter Number "+str(counter)+": "))
    sum1+=Number
    if(Number>max1):
        max1=Number
    if(Number<min1):
        min1=Number
    counter += 1
print("average = ",end="")
print(sum1/10) 
print("max = ",end="")
print(max1)
print("min = ",end="")
print(min1)  
