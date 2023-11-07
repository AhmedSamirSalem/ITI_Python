File=open("Config.c","w")
File.write('''void DDRA_init(void)
{
    DDRA=0b''')
i=0
Reg_value=""
while i <8 :
    Mode=input("Please Enter Bit "+str(i)+" Mode: ")
    if  Mode.lower() == "input":
        # File.write("0")
        Reg_value='0'+Reg_value
        # Reg_value&=~(1<<i)
    elif Mode.lower() == "output":
        # File.write("1")
        Reg_value='1'+Reg_value
        # Reg_value|=(1<<i)
    else:
        # File.write("0")
        Reg_value='0'+Reg_value
        # Reg_value*=10+0
    i+=1
File.write(str(Reg_value))    
File.write(";\n}")
File.close()