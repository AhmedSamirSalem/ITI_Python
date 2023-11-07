rows = int(input("Please Enter Number of Rows: "))
counter = 0
while counter < rows:
    # space counter
    print(" " * (rows - counter - 1), end="")
    # Star Counter
    print((counter*2+1) * "*")
    counter += 1
counter = 1
while counter < rows:
    # space counter
    print(" " * counter, end="")
    # Star Counter
    print(((rows-1-counter) * 2+1) * "*")
    counter += 1
