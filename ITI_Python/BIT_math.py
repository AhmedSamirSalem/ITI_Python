def SET_BIT(reg, bit) :
        reg|=(1<<bit)
        return reg    
def CLEAR_BIT(reg, bit):
        reg&=~(1<<bit)
        return reg
def TOGGLE_BIT(reg, bit) :
        reg^=(1<<bit)
        return reg
def GET_BIT(reg, bit): 
        return((reg>>bit)&1)
         
x=0
x=SET_BIT(x,0)
x=CLEAR_BIT(x,0)
x=TOGGLE_BIT(x,0)
x=GET_BIT(x,0)
x=SET_BIT(x,1)
x=SET_BIT(x,2)

print(x)

