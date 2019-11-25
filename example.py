from tkinter import *

root = Tk()

def fnB(*args):
    print("QQ",*args)


Butt1 = Button(root,command=root.quit,text="Butt ON")
Butt1.grid()

root.mainloop()
root.destroy()
