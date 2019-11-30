from tkinter import *

root = Tk()

def dump(*args):
    print("DUMP:",*args)


Butt1 = Button(root,text="Butt ON")
Butt1.grid(row=0,column=0)
Butt1.bind("<Button-1>",dump)

Exit = Button(root,command=root.quit,text="Exit")
Exit.grid(row=0,column=1)

Txt = Label(root,text="This is a label",bg="green",fg="red")
Txt.grid(row=1,column=0)

root.mainloop()
#root.destroy()
