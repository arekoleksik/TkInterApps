from tkinter import *
from tkinter import messagebox
import random

zmieniacz = True

def losowe():
    return random.randint(1,9)


def pokaz():
    messagebox.showinfo('',"ZWYCIĘSTWO! GRATULACJE!")


def znakx(b):
    pass
    
    '''global l, zmieniacz
    if zmieniacz == True:
        l = Label(b, text='X' ,fg ='red',font = ("Arial", "20", "bold"))
        l.grid(column=0)
        #b.config(height=5, width=10)
        

    else:
        l = Label(b, text='O' ,fg ='green',font = ("Arial", "20", "bold"))
        l.grid(column=0)
        #b.config(height=5, width=10)
        #b.config(text='O' ,fg ='green',font = ("Arial", "20", "bold"))
    zmieniacz = not zmieniacz'''

def Ruch(b):
    
    if b["text"] == "":
        b.config(text="X",fg ='red',font = ("Arial", "9", "bold"))
        gdzie = b.grid_info()
        ruch = (gdzie["row"], gdzie["column"])
        print (ruch)
        return ruch
    


root = Tk()

frame = Frame(root)
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, height=3, width=7, text="", command=lambda i=i, j=j: Ruch(buttons[i][j]))
        buttons[i][j].grid(row=i, column=j)

'''lf1 = LabelFrame(root,width=200,height=200,bg='white')
lf1.grid(column = 0, row= 0)

b1 = Button(lf1,text=" ",command=lambda:znakx(b1))
b1.grid(column = 0, row= 0)


b2 = Button(root,text=" ",command=lambda:znakx(b2))
b2.grid(column = 1, row= 0)

b3 = Button(root,text=" ",command=lambda:znakx(b3))
b3.grid(column = 2, row= 0)

b4 = Button(root,text='',command=lambda:znakx(b4))
b4.grid(column = 0, row= 1)

b5 = Button(root,text='',command=lambda:znakx(b5))
b5.grid(column = 1, row= 1)

b6 = Button(root,text='',command=lambda:znakx(b6))
b6.grid(column = 2, row= 1)

b7 = Button(root,text='',command=lambda:znakx(b7))
b7.grid(column = 0, row= 2)

b8 = Button(root,text='',command=lambda:znakx(b8))
b8.grid(column = 1, row= 2)

b9 = Button(root,text='',command=lambda:znakx(b9))
b9.grid(column = 2, row= 2)'''


root.mainloop()

