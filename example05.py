'''
    Пример работы с редактируемым текстом
'''

from tkinter import *


def dump(*args):
    print("DUMP:",*args)

def GetText():
    print(txt.get())

def PutText():
    t = txt.get()
    txt2.delete(0,END)
    txt2.insert(0,t)

TKroot = Tk()
TKroot.title("Text")    #окно

root = Frame(TKroot)    #рамка
root.grid()

txt = Entry(root,text="Text")   #текстовое поле1
txt.grid(columnspan=2)
txt2 = Entry(root,text="Text2")   #текстовое поле2
txt2.grid(columnspan=2)

getButton = Button(root,text="Get", command = GetText)
getButton.grid()
putButton = Button(root,text="Put", command = PutText)
putButton.grid(column=1,row=2)

TKroot.mainloop()

