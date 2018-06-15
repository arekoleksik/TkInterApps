from tkinter import *
from tkinter import messagebox
import random

l = []
l2=[]

#generowanie liczb
def losowe():
    return random.randint(1,999)

for i in range (25):
    l.append(losowe())
#print(l)

def pokaz():
    messagebox.showinfo('',"ZWYCIĘSTWO! GRATULACJE!")


def znikacz(n, z):
    global l
    min = 1000
    m = l[n]
    #print(m)
    #minimalna wartość z listy
    for i in range (len(l)):
        if min > l[i] and l[i] not in l2:
            min = l[i]
        #print(min)
            
    #jesli trafisz dezaktywuj Button i dodaj do l2, jeśli l2 ma 25 poz. zakończ grę       
    if min == m:
        z.config(state = 'disabled')
        l2.append(m)
        if len(l2) == 25:
            pokaz()
        #print(l2)    
    
root = Tk()        

b1 = Button(root,text=l[0],width=10, command = lambda: znikacz(0, b1))
b1.grid(column = 0, row= 0)

b2 = Button(root,text=l[1],width=10, command = lambda: znikacz(1, b2))
b2.grid(column = 1, row= 0)

b3 = Button(root,text=l[2],width=10,command = lambda: znikacz(2, b3))
b3.grid(column = 2, row= 0)

b4 = Button(root,text=l[3],width=10,command = lambda: znikacz(3, b4))
b4.grid(column = 3, row= 0)

b5 = Button(root,text=l[4],width=10,command = lambda: znikacz(4, b5))
b5.grid(column = 4, row= 0)

b6 = Button(root,text=l[5],width=10,command = lambda: znikacz(5, b6))
b6.grid(column = 0, row= 1)

b7 = Button(root,text=l[6],width=10,command = lambda: znikacz(6, b7))
b7.grid(column = 1, row= 1)

b8 = Button(root,text=l[7],width=10,command = lambda: znikacz(7, b8))
b8.grid(column = 2, row= 1)

b9 = Button(root,text=l[8],width=10,command = lambda: znikacz(8, b9))
b9.grid(column = 3, row= 1)

b10 = Button(root,text=l[9],width=10,command = lambda: znikacz(9, b10))
b10.grid(column = 4, row= 1)

b11 = Button(root,text=l[10],width=10,command = lambda: znikacz(10, b11))
b11.grid(column = 0, row= 2)

b12 = Button(root,text=l[11],width=10,command = lambda: znikacz(11, b12))
b12.grid(column = 1, row= 2)

b13 = Button(root,text=l[12],width=10,command = lambda: znikacz(12, b13))
b13.grid(column = 2, row= 2)

b14 = Button(root,text=l[13],width=10,command = lambda: znikacz(13, b14))
b14.grid(column = 3, row= 2)

b15 = Button(root,text=l[14],width=10,command = lambda: znikacz(14, b15))
b15.grid(column = 4, row= 2)

b16 = Button(root,text=l[15],width=10,command = lambda: znikacz(15, b16))
b16.grid(column = 0, row= 3)

b17 = Button(root,text=l[16],width=10,command = lambda: znikacz(16, b17))
b17.grid(column = 1, row= 3)

b18 = Button(root,text=l[17],width=10,command = lambda: znikacz(17, b18))
b18.grid(column = 2, row= 3)

b19 = Button(root,text=l[18],width=10,command = lambda: znikacz(18, b19))
b19.grid(column = 3, row= 3)

b20 = Button(root,text=l[19],width=10,command = lambda: znikacz(19, b20))
b20.grid(column = 4, row= 3)

b21 = Button(root,text=l[20],width=10,command = lambda: znikacz(20, b21))
b21.grid(column = 0, row= 4)

b22 = Button(root,text=l[21],width=10,command = lambda: znikacz(21, b22))
b22.grid(column = 1, row= 4)

b23 = Button(root,text=l[22],width=10,command = lambda: znikacz(22, b23))
b23.grid(column = 2, row= 4)

b24 = Button(root,text=l[23],width=10,command = lambda: znikacz(23, b24))
b24.grid(column = 3, row= 4)

b25 = Button(root,text=l[24],width=10,command = lambda: znikacz(24, b25))
b25.grid(column = 4, row= 4)

root.mainloop()

