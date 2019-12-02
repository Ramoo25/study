'''
    Пример работы с редактируемым текстом
'''

#MORE JUNK COMMIT

from tkinter import *


def dump(*args):
    print("DUMP:",*args)

def GetText():
    print(txt.get())

def PutText():
    t = txt.get()
    str2.set(t)

def txt2_in(*args):
    print(str2.get())

TKroot = Tk()
TKroot.title("Text")    #окно

root = Frame(TKroot)    #рамка
root.grid()

txt = Entry(root,text="Text")   #текстовое поле1
txt.grid(columnspan=2)
str2 = StringVar()
str2.trace("w",txt2_in)
txt2 = Entry(root,text="Text2",textvariable=str2)   #текстовое поле2
txt2.grid(columnspan=2)


getButton = Button(root,text="Get", command = GetText)
getButton.grid()
putButton = Button(root,text="Put", command = PutText)
putButton.grid(column=1,row=2)

TKroot.mainloop()
