'''
    Пример работы с редактируемым текстом
'''

from tkinter import *


def dump(*args):
    print("DUMP:",*args)


TKroot = Tk()
TKroot.title("Text")    #окно

root = Frame(TKroot)    #рамка
root.grid()

txt = Entry(root,text="Text")   #текстовое поле
txt.grid()

def GetText():
    print(txt.get())

get = Button(root,text="Get", command = GetText)
get.grid()

TKroot.mainloop()


'''
root = Frame(TKroot)
root.place(relx=0,rely=0,relheight=1,relwidth=1)

root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.rowconfigure(0,weight = 1)
root.rowconfigure(1,weight = 0)


Butt1 = Button(root,text="Butt ON")
Butt1.grid(row=0,column=0,sticky=E+W+S+N)
Butt1.bind("<Button-1>",dump)

Exit = Button(root,command=root.quit,text="Exit")
Exit.grid(row=0,column=1,sticky=E+W+S+N)

Txt = Label(root,text="This is a label",bg="PeachPuff",fg="red")
Txt.grid(row=1,column=0,columnspan=2,sticky=E+W+N)

TKroot.mainloop()
#root.destroy()
'''
