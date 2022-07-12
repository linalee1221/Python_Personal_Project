from tkinter import *

#### 창 설정부
root = Tk()
root.configure(width="70m", height="100m")

#### 함수 부
def Add():
    result = int(E1.get()) + int(E2.get())
    Lb1 = Label(root, text=str(result))
    Lb1.place(x=80, y=110, width=100, height=40)
    


def Sub():
    result = int(E1.get()) - int(E2.get())
    Lb1 = Label(root, text=str(result))
    Lb1.place(x=80, y=110, width=100, height=40)
    
def Mul():
    result = int(E1.get()) * int(E2.get())
    Lb1 = Label(root, text=str(result))
    Lb1.place(x=80, y=110, width=100, height=40)

def Div():
    result = int(E1.get()) / int(E2.get())
    Lb1 = Label(root, text=str(result))
    Lb1.place(x=80, y=110, width=100, height=40)

def Rmd():
    result = int(E1.get()) % int(E2.get())
    Lb1 = Label(root, text=str(result))
    Lb1.place(x=80, y=110, width=100, height=40)
    
#### 창 부품부
E1 = Entry(root)
E1.place(x=10, y=10, width=100, height=30)
E2 = Entry(root)
E2.place(x=140, y=10, width=100, height=30)

Button(root, text="+", command=Add).place(x=16, y=60, width=30, height=30)
Button(root, text="-", command=Sub).place(x=66, y=60, width=30, height=30)
Button(root, text="*", command=Mul).place(x=116, y=60, width=30, height=30)
Button(root, text="/", command=Div).place(x=166, y=60, width=30, height=30)
Button(root, text="%", command=Rmd).place(x=216, y=60, width=30, height=30)

Lb1 = Label(root, text="test")
Lb1.place(x=80, y=110, width=100, height=40)

root.mainloop()
