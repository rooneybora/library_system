from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Student')
        self.canvas = Canvas(width=500, height=417)
        self.canvas.pack()
        self.resizable(0,0)
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+100
            r=r+1000
        n = StringVar()
        p = StringVar()
        a = StringVar()
#verifying input
        def asi():
            if len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Admission")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Form")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    name1 = n.get()
                    adm1 = p.get()
                    fm1 = a.get()
                    self.myCursor.execute("Insert into student(name,admission,form) values (%s,%s,%s)",[name1,adm1,fm1])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add_Student.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","something is wrong")

        # label and input box
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_remove.png'))
        self.lbl = Label(self, text='Student Details',bg="#"+c, fg="#"+c, font=('Calibri', 25, 'bold')).pack()
        self.lbl1 =Label(self, text='Name:',bg="#"+c, font=('Calibri', 10, 'bold')).place(x=70, y=82)
        self.ent =Entry(self, textvariable=n, width=30).place(x=200, y=84)
        self.lbl2 =Label(self, text='Admission:',bg="#"+c, font=('Calibri', 10, 'bold')).place(x=70, y=130)
        self.ent1 = Entry(self, textvariable=p, width=30).place(x=200, y=132)
        self.lbl3 = Label(self, text='Form:',bg="#"+c, font=('Calibri', 10, 'bold')).place(x=70, y=180)
        self.ent2 =Entry(self, textvariable=a, width=30).place(x=200, y=182)
        self.btn =Button(self,image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0,command=asi)
        self.btn.photo = img
        self.btn.place(x=230, y=220)

Add().mainloop()
