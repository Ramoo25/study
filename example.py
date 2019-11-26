from tkinter import *

root = Tk()

def dump(*args):
    print("DUMP:",*args)


Butt1 = Button(root,text="Butt ON")
Butt1.grid()
Butt1.bind("<Button-1>",dump)

Exit = Button(root,command=root.quit,text="Exit")
Exit.grid()


root.mainloop()
root.destroy()
