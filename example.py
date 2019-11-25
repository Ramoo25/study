from tkinter import *

root = Tk()

def fnB(*args):
    print("QQ",*args)


Butt = Button(root,text="Butt ON")
Butt.bind("<Button 1>",fnB)
Butt.grid()

root.mainloop()
print("QQ")
