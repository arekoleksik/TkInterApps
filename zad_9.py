from tkinter import *

def Wynik():
    global l
    a = przeł1.get()* przeł2.get()
    
    r = 255-(25*przeł1.get())
    g = 255-(25*przeł2.get())
    b = przeł1.get()*25
    kolor = "#%02x%02x%02x" % (r,g,b)
    
    l.config(text=str(a), fg = kolor)
    
root = Tk()        

# RB poziome
przeł1=IntVar()

c11 = Radiobutton(root,text="1", variable = przeł1, value = 1, command=Wynik)
c11.select()
c11.grid(column = 1, row= 0)

c12 = Radiobutton(root,text="2", variable = przeł1, value = 2, command=Wynik)
c12.grid(column = 2, row= 0)

c13 = Radiobutton(root,text="3", variable = przeł1, value = 3, command=Wynik)
c13.grid(column = 3, row= 0)

c14 = Radiobutton(root,text="4", variable = przeł1, value = 4, command=Wynik)
c14.grid(column = 4, row= 0)

c15 = Radiobutton(root,text="5", variable = przeł1, value = 5, command=Wynik)
c15.grid(column = 5, row= 0)

c16 = Radiobutton(root,text="6", variable = przeł1, value = 6, command=Wynik)
c16.grid(column = 6, row= 0)

c17 = Radiobutton(root,text="7", variable = przeł1, value = 7, command=Wynik)
c17.grid(column = 7, row= 0)

c18 = Radiobutton(root,text="8", variable = przeł1, value = 8, command=Wynik)
c18.grid(column = 8, row= 0)

c19 = Radiobutton(root,text="9", variable = przeł1, value = 9, command=Wynik)
c19.grid(column = 9, row= 0)

c10 = Radiobutton(root,text="10", variable = przeł1,value=10, command=Wynik)
c10.grid(column = 10, row= 0)


# RB pionowe
przeł2=IntVar()

c21 = Radiobutton(root,text="1", variable = przeł2,value = 1, command=Wynik)
c21.select()
c21.grid(column = 0, row= 1)

c22 = Radiobutton(root,text="2", variable = przeł2,value = 2, command=Wynik)
c22.grid(column = 0, row= 2)

c23 = Radiobutton(root,text="3", variable = przeł2,value = 3, command=Wynik)
c23.grid(column = 0, row= 3)

c24 = Radiobutton(root,text="4", variable = przeł2,value = 4, command=Wynik)
c24.grid(column = 0, row= 4)

c25 = Radiobutton(root,text="5", variable = przeł2,value = 5, command=Wynik)
c25.grid(column = 0, row= 5)

c26 = Radiobutton(root,text="6", variable = przeł2,value = 6, command=Wynik)
c26.grid(column = 0, row= 6)

c27 = Radiobutton(root,text="7", variable = przeł2,value = 7, command=Wynik)
c27.grid(column = 0, row= 7)

c28 = Radiobutton(root,text="8", variable = przeł2,value = 8, command=Wynik)
c28.grid(column = 0, row= 8)

c29 = Radiobutton(root,text="9", variable = przeł2,value = 9, command=Wynik)
c29.grid(column = 0, row= 9)

c20 = Radiobutton(root,text="10", variable = przeł2,value = 10, command=Wynik)
c20.grid(column = 0, row= 10)


#Lebel
l = Label(root, text = 0 ,fg = 'black', font = ("Arial", "70", "bold"))
l.grid(column = 4, row= 4, columnspan = 4, rowspan =4)

root.mainloop()
