from tkinter import *

root = Tk()
root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.rowconfigure(0,weight = 1)

def dump(*args):
    print("DUMP:",*args)


Butt1 = Button(root,text="Butt ON")
Butt1.grid(row=0,column=0,sticky=E+W)
Butt1.bind("<Button-1>",dump)

Exit = Button(root,command=root.quit,text="Exit")
Exit.grid(row=0,column=1,sticky=E+W)

Txt = Label(root,text="This is a label",bg="PeachPuff",fg="red")
Txt.grid(row=1,column=0,columnspan=2,sticky=E+W)

root.mainloop()
#root.destroy()
