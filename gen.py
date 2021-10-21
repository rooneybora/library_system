from barcode import EAN13
from barcode.writer import ImageWriter
from tkinter import *

bargen = Tk()
bargen.title("bargen")

a=StringVar()
b=int()

ent = Entry(bargen,textvariable=a)
ent.place(x=50,y=50)

ent1 = Entry(bargen,textvariable=b)
ent1.place(x=50,y=70)



mycode = EAN13(int(b.get()),writer=ImageWriter())
mycode.save(a.get())

bargen.mainloop()