from tkinter import *

root = Tk()
root.geometry('800x600')
c = Canvas(root, width=800, height=600, bg = 'white')

#kadłub
c.create_line(150,450,650,450,700,350, 100, 350, 150, 450, fill='red',width = 2)
c.grid(row=0)

#flaga
c.create_line(115,350,115,325,fill='red',width = 2)
c.create_rectangle(115,325,60,315,fill='red', outline = 'red',width = 2)
c.create_rectangle(115,315,60,303,fill='white', outline = 'red',width = 2)

#maszty
c.create_rectangle(285, 350, 300, 275, outline = 'red',width = 2)
c.create_rectangle(285, 25, 300, 100, outline = 'red',width = 2)
c.create_rectangle(510, 350, 525, 25, outline = 'red',width = 2)

#żagle
c.create_rectangle(200,100,385,275, outline = 'red',width = 2)

c.create_polygon(525,35,650,100,525,165,outline = 'red',fill='white',width = 2)
c.create_polygon(525,165,650,230,525,295,outline = 'red',fill='white',width = 2)

#bulaje
c.create_oval(525,375,565,415,outline = 'red',fill='white',width = 2)
c.create_oval(585,375,625,415,outline = 'red',fill='white',width = 2)

#ster
c.create_oval(180,285,220,325,outline = 'orange',fill='white',width = 2)
c.create_line(200,280,200,350,fill='orange',width = 2)
c.create_line(180,280,220,330,fill='orange',width = 2)
c.create_line(180,330,220,280,fill='orange',width = 2)
c.create_line(175,305,225,305,fill='orange',width = 2)

#tekst
c.create_text(200, 400, text = 'TSR 2017', font =('Arial','14'))

#fale
x1= 0
x2=50

for i in range (16):
    c.create_arc(x1, 450,x2,500, outline = 'blue', width=2,style=ARC, start=0, extent= 180) 
    x1 += 50
    x2 += 50

root.mainloop()
