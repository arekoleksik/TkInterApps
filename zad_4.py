from tkinter import *
import random

def ucieczka(s = None):
    b1.place(x=random.randint(0,460))
    b1.place(y=random.randint(0,480))  

root = Tk()
root.geometry('500x500')

b1 = Button(root,text='Złap mnie!')
b1.place(x=20,y=20)
b1.bind('<Enter>',ucieczka)

root.mainloop()
