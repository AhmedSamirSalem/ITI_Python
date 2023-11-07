from tkinter import * 


def Fuc() :
    print("Hello")
root=Tk()
root.title("Ahmed")
root.geometry("400x400+100+100")

b1=Button(root,text="Exit",bd=5,bg="red",command=root.destroy)
b1.grid(row=1,column=0)

b2=Button(root,text="print",command=Fuc)
b2.grid(row=0,column=1)

b3=Button(root,text="Exit",command=root.destroy)
b3.grid(row=2,column=1)

b4=Button(root,text="Exit",command=root.destroy)
b4.grid(row=1,column=2)

root.mainloop()