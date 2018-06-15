from tkinter import *


def mryg():
    global kolor, r, g, y, kol1,kol2,kol3
    r= c.create_oval(60,50,135,125, fill='gray')
    y= c.create_oval(60,150,135,225,fill='gray')
    g= c.create_oval(60,250,135,325,fill='gray')
    if kolor == 1:
        c.itemconfig(r, fill=kol1)
        kolor+=1
        c.after(1000,mryg)
        
    elif kolor == 2:
        c.itemconfig(r, fill=kol1)
        c.itemconfig(y, fill=kol2)
        kolor+=1
        c.after(1000,mryg)

    elif kolor == 3:
        c.itemconfig(g, fill=kol3)
        kolor+=1
        c.after(1000,mryg)

    elif kolor == 4:
        c.itemconfig(y, fill=kol2)
        kolor = 1
        c.after(1000,mryg)

kolor = 1
o = Tk()
o.geometry("200x400")
c = Canvas(o,width=200, height=400)
c. pack()
c.after(1000,mryg)
kol1 = 'red'
kol2 = 'yellow'
kol3= 'green'

o.mainloop()
