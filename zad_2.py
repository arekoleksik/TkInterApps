from tkinter import *
from tkinter import messagebox

def tylkocyfry(*a):
    global e11, wpis
    s = e11.get()
    if s == '' or s.isdigit():
        wpis = s
    else:
        e11.set(wpis)
        
def tylkocyfry2(*a):
    global e12, wpis2
    s = e12.get()
    if s == '' or s.isdigit():
        wpis2 = s
    else:
        e12.set(wpis2)

def dodawanie():
    if len(wpis) and len (wpis2)!= 0:
        wynik = float(wpis)+ float(wpis2)
        print(r)
        return wynik
        

def odejmowanie():
    if len(wpis) and len(wpis2) != 0:
        wynik = float(wpis)- float(wpis2)
        print (wpis, wpis2)
        print (wynik)
        print(r)
        return wynik
        
 
    
def mnozenie():
    if len(wpis) and len (wpis2) != 0:
        wynik = float(wpis)*float(wpis2)
        print (wpis, wpis2)
        print (wynik)
        print(r)
        return wynik
        global wynik

def dzielenie():
    if len(wpis) and len (wpis2) != 0:
        try:
            wynik = float(wpis)/ float(wpis2)
            print (wpis, wpis2)
            print (wynik)
            print(r)
            return wynik
            global wynik
        except ZeroDivisionError:
            blad()
def blad():
    wynik = 'blad'
    global wynik           
    
def sprawdz():
    if wynik == 'blad':
        messagebox.showerror("Błąd", "Dzielisz przez zero!")
        e2.focus_set()
    elif wynik == 0:
        messagebox.showinfo("Wynik", '0')
    else:
        messagebox.showinfo("Wynik", wynik)



wynik = ''    
wpis = ''
wpis2 = ''
root = Tk()

e11 = StringVar()
e11.set(wpis)
e1 = Entry(root, width = 10,textvariable = e11)
e1.grid(column = 0, row = 2)
e1.focus_set()

e12 = StringVar()
e12.set(wpis2)
e2 = Entry(root, width = 10,textvariable = e12)
e2.grid(column = 2, row = 2)

e11.trace('w', tylkocyfry)
e12.trace('w', tylkocyfry2)

r = IntVar()
r1 = Radiobutton(root, text = '+', variable = r, value = 1, command = dodawanie).grid(column = 1, row = 0)
r2 = Radiobutton(root, text = '-', variable = r, value = 2, command = odejmowanie).grid(column = 1, row = 1)
r3 = Radiobutton(root, text = '*', variable = r, value = 3, command = mnozenie).grid(column = 1, row = 2)
r4 = Radiobutton(root, text = '/', variable = r, value = 4, command = dzielenie).grid(column = 1, row = 3)

b1 = Button (root, text='Oblicz', command = sprawdz).grid(column = 1, row = 4)



root.mainloop()
