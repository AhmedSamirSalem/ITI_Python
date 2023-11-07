name="Ahmed"
#antoher way more easy to reverse the string
#print(name[::-1])
counter=1
for i in name:
    print(name[len(name)-counter],end="")
    counter+=1

# print(name[-1:len(name)*-1-1:-1])