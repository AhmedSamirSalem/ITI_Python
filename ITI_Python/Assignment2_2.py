Number=int(input("Please Enter Number To Calculate its factorial: "))
factorial=1
while Number > 0:
	factorial=factorial*Number
	Number-=1
print("Factorial= "+str(factorial))
