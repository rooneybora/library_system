from tkinter import *
from tkinter import messagebox
import re
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
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
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",[u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
#label and input
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_remove.png'))
        Label(self, text='User Details', bg="#"+c, fg='black', font=('Calibri', 25, 'bold')).place(x=130, y=22)
        Label(self, text='Username:', bg="#"+c, font=('Calibri', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='Name:', bg="#"+c, font=('Calibri', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='Password:', bg="#"+c, font=('Calibri', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        self.btn = Button(self, image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0, command=insert)
        self.btn.photo = img
        self.btn.place(x=230, y=220)
reg().mainloop()