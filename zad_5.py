from tkinter import *

def przesunlewo(s = None):
    global x1
    if x1 != 0:
        x1 -= 1 
        b1.place(x=x1)
        #print(x1)
        
def przesunprawo(s=None):
    global x1
    if x1 != 480:
        x1 += 1
        b1.place(x=x1)
        #print(x1)

def przesunlewo2(s = None):
    global x1
    if x1 != 0:
        x1 -= 5
        b1.place(x=x1)
        #print(x1)
        
def przesunprawo2(s=None):
    global x1
    if x1 != 480:
        x1 = x1 + 5
        b1.place(x=x1)
        #print(x1)

def koniec(s=None):
    root.destroy()
    
x1= 240
root = Tk()
root.geometry('500x500')

b1 = Button(root,bitmap='questhead')
b1.place(x=x1, y =240)
b1.focus_set()

b1.bind('<Left>',przesunlewo)
b1.bind('<Right>',przesunprawo)

b1.bind('<Control-Left>',przesunlewo2)
b1.bind('<Control-Right>',przesunprawo2)

b1.bind('<Escape>',koniec)

root.mainloop()
