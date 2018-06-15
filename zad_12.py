from tkinter import *


def obserwator(*a):
   wez_input()
   print('obserwator')

def wez_input():
    inputValue=text.dump("1.0","end-1c")
    print(inputValue)


root = Tk()
root.title("Text")

napis = StringVar()

text = Text(root)
text.grid(row=0, column=0, columnspan=3)
text.insert(END,'1234')

napis.set(text.get(1.0, END))
wez_input()


print(napis.get())
o = napis.trace('w', obserwator)




e1 = Entry(root, textvariable=napis, state = 'readonly').grid(row=1, column=0)

e2 = Entry(root).grid(row=1, column=1)
e3 = Entry(root).grid(row=1, column=2)
root.mainloop()
