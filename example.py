from tkinter import *

root = Tk()

def fnB(*args):
    print("QQ",args)


Butt = Button(root,command = fnB,text="Butt ON")
Butt.grid()

root.mainloop()
print("QQ")
