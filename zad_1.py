from tkinter import *
from tkinter import messagebox

def cyfry (*a):
    global wpis, tw
    s = tw.get()
    if s == '' or s.isdigit():
        wpis = s
    else:
        tw.set(wpis) 
        
def kontrolna (wpis):
    if len (wpis) != 11:
        return False
    else:
        p = int(wpis[0])+ 3*int(wpis[1])+ 7*int(wpis[2])+ \
            9*int(wpis[3])+ int(wpis[4])+ 3*int(wpis[5])+ \
            7*int(wpis[6])+ 9*int(wpis[7])+ int(wpis[8])+ \
            3*int(wpis[9])+ int(wpis[10])
        if p % 10 != 0:
            return False
        else:
            return True
   
def sprawdz():
    if kontrolna(wpis)== True:
        messagebox.showinfo("", "Warość prawidłowa")
    else:
        messagebox.showerror("Błąd", "To nie jest nr PESEL!")     

wpis = ''
okno = Tk()
okno.title("")
tw = StringVar()

l1 = Label(okno, text = "PESEL:")
l1.grid(column=0, row=0)

e1 = Entry(okno, width=11, textvariable = tw)
e1.grid(column=1, row=0)
e1.focus_set()

b1= Button(okno, text = "Sprawdź!", command = sprawdz)
b1.grid(row = 1, columnspan=2)

tw.set(wpis)
tw.trace('w',cyfry)

okno.mainloop()
