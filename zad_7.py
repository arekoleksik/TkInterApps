from tkinter import *

def Koniec():
    root.destroy()

def Wynik():
    if przeł0.get() == 0:
        zero = 0
    elif przeł0.get() == 1:
        zero = 1
        
    a = zero+((przeł1.get()*2)**1)+\
        ((przeł2.get()*2)**2)+((przeł3.get()*2)**3)+\
        ((przeł4.get()*2)**4)+((przeł5.get()*2)**5)+\
        ((przeł6.get()*2)**6)+((przeł7.get()*2)**7)
    l.config(text=str(a))
    
root = Tk()        

koniec = Button(root,text='Koniec',width=10, command = Koniec)
koniec.grid(column = 3, row= 2, columnspan = 2)

przeł0=IntVar()
c0 = Checkbutton(root,text="0", variable = przeł0, command=Wynik)
c0.grid(column = 7, row= 0)

przeł1=IntVar()
c1 = Checkbutton(root,text="1", variable = przeł1,command=Wynik)
c1.grid(column = 6, row= 0)

przeł2=IntVar()
c2 = Checkbutton(root,text="2", variable = przeł2, command=Wynik)
c2.grid(column = 5, row= 0)

przeł3=IntVar()
c3 = Checkbutton(root,text="3", variable = przeł3,command=Wynik)
c3.grid(column = 4, row= 0)

przeł4=IntVar()
c4 = Checkbutton(root,text="4", variable = przeł4,command=Wynik)
c4.grid(column = 3, row= 0)

przeł5=IntVar()
c5 = Checkbutton(root,text="5", variable = przeł5,command=Wynik)
c5.grid(column = 2, row= 0)

przeł6=IntVar()
c6 = Checkbutton(root,text="6", variable = przeł6,command=Wynik)
c6.grid(column = 1, row= 0)

przeł7=IntVar()
c7 = Checkbutton(root,text="7", variable = przeł7,command=Wynik)
c7.grid(column = 0, row= 0)

l = Label(root, text = 0 ,fg = 'blue', font = ("Arial", "34", "bold"))
l.grid(column = 3, row= 1, columnspan = 2)

root.mainloop()
